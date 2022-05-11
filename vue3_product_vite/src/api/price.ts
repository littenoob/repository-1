import request from '@/api/request';
type unableVar = null | undefined
export function SearchphoneResult(key:string) {
    if (key) {
        return request.get('/brand/'+key)
    }
}
export function PriceDays(days:number,brand:string|unableVar,tablename:string) {
    if (brand && tablename) {
        const params = {
            days,
            brand
        }
        return request.get('/api/v0.1/price/'+tablename,params as any)
    }
}