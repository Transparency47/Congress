# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1325
- Title: Expressing support for May 2026 as "American Stroke Month" and encouraging all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.
- Congress: 119
- Bill type: HRES
- Bill number: 1325
- Origin chamber: House
- Introduced date: 2026-05-29
- Update date: 2026-05-30T08:18:25Z
- Update date including text: 2026-05-30T08:18:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-29: Introduced in House
- 2026-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-29 - IntroReferral: Submitted in House
- Latest action: 2026-05-29: Submitted in House

## Actions

- 2026-05-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-29 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-29",
    "latestAction": {
      "actionDate": "2026-05-29",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1325",
    "number": "1325",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001281",
        "district": "3",
        "firstName": "Joyce",
        "fullName": "Rep. Beatty, Joyce [D-OH-3]",
        "lastName": "Beatty",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expressing support for May 2026 as \"American Stroke Month\" and encouraging all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.",
    "type": "HRES",
    "updateDate": "2026-05-30T08:18:25Z",
    "updateDateIncludingText": "2026-05-30T08:18:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-05-29T16:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "TN"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1325ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1325\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2026 Mrs. Beatty (for herself and Mr. Cohen ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for May 2026 as American Stroke Month and encouraging all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.\nThat the House of Representatives expresses support for American Stroke Month and encourages all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.",
      "versionDate": "2026-05-29",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1325ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for May 2026 as \"American Stroke Month\" and encouraging all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T08:18:25Z"
    },
    {
      "title": "Expressing support for May 2026 as \"American Stroke Month\" and encouraging all to learn the warning signs of stroke, understand their personal risk factors, and take action to improve stroke prevention, response, and recovery in our communities.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T08:06:08Z"
    }
  ]
}
```
