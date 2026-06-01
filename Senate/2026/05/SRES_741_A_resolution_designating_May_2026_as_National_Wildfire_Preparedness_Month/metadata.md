# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/741
- Title: A resolution designating May 2026 as "National Wildfire Preparedness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 741
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-27T05:03:26Z
- Update date including text: 2026-05-27T05:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2419)
- 2026-05-20 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-20: Submitted in Senate

## Actions

- 2026-05-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S2419)
- 2026-05-20 - IntroReferral: Submitted in Senate

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
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/741",
    "number": "741",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution designating May 2026 as \"National Wildfire Preparedness Month\".",
    "type": "SRES",
    "updateDate": "2026-05-27T05:03:26Z",
    "updateDateIncludingText": "2026-05-27T05:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S2419)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
          "date": "2026-05-20T14:49:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres741is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 741\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Ms. Hirono submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating May 2026 as National Wildfire Preparedness Month .\nThat the Senate\u2014\n**(1)**\ndesignates May 2026 as National Wildfire Preparedness Month ;\n**(2)**\nencourages increased awareness of, and preparedness for, the threat of wildfires and subsequent suppression efforts at the Federal, State, local, and Tribal levels of government, including Alaska Native and Native Hawaiian communities, and by nongovernmental organizations and communities; and\n**(3)**\nsupports resources and educational initiatives that communicate how communities at risk of exposure to wildfire hazards can take preventative measures, including home hardening, land management practices that reduce or remove highly flammable grasses and shrubs, instituting or enhancing early warning systems, reducing unplanned human ignitions, reducing adverse health impacts from smoke and fire exposure, and safely and efficiently evacuating people and their animals.",
      "versionDate": "2026-05-20",
      "versionType": "IS"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres741is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution designating May 2026 as \"National Wildfire Preparedness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T05:03:26Z"
    },
    {
      "title": "A resolution designating May 2026 as \"National Wildfire Preparedness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:34Z"
    }
  ]
}
```
