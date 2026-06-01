# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1308?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1308
- Title: Designating May 2026 as "National Wildfire Preparedness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1308
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-22T02:18:39Z
- Update date including text: 2026-05-22T02:18:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-20 - IntroReferral: Submitted in House
- Latest action: 2026-05-20: Submitted in House

## Actions

- 2026-05-20 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1308",
    "number": "1308",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Designating May 2026 as \"National Wildfire Preparedness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-22T02:18:39Z",
    "updateDateIncludingText": "2026-05-22T02:18:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
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
          "date": "2026-05-20T15:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1308ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1308\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2026 Mrs. Torres of California (for herself, Mr. Obernolte , and Mr. Valadao ) submitted the following resolution; which was referred to the Committee on Natural Resources\nRESOLUTION\nDesignating May 2026 as National Wildfire Preparedness Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Wildfire Preparedness Month ;\n**(2)**\nencourages increased awareness of, and preparedness for, the threat of wildfires and subsequent suppression efforts at the Federal, State, local, and Tribal levels of government, including Alaska Native and Native Hawaiian communities, and by nongovernmental organizations and communities; and\n**(3)**\nsupports resources and educational initiatives that communicate how communities at risk of exposure to wildfire hazards can take preventative measures, including, home hardening, land management practices that reduce or remove highly flammable grasses and shrubs, instituting or enhancing early warning systems, reducing unplanned human ignitions, reducing adverse health impacts from smoke and fire exposure, and safely and efficiently evacuating people and their animals.",
      "versionDate": "2026-05-20",
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
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1308ih.xml"
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
      "title": "Designating May 2026 as \"National Wildfire Preparedness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:39Z"
    },
    {
      "title": "Designating May 2026 as \"National Wildfire Preparedness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:08:40Z"
    }
  ]
}
```
