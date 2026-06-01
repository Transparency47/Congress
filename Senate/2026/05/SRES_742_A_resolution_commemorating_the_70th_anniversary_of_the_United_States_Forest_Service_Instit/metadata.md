# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/742
- Title: A resolution commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.
- Congress: 119
- Bill type: SRES
- Bill number: 742
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-27T05:03:26Z
- Update date including text: 2026-05-27T05:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2419)
- 2026-05-20 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-20: Submitted in Senate

## Actions

- 2026-05-20 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2419)
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/742",
    "number": "742",
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
    "title": "A resolution commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
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
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2419)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
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
          "date": "2026-05-20T15:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres742is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 742\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Ms. Hirono (for herself and Mr. Schatz ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nRESOLUTION\nCommemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.\nThat the Senate\u2014\n**(1)**\ncommemorates the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry (referred to in this resolution as the IPIF );\n**(2)**\nrecognizes the vital contributions that the research conducted and data produced by the IPIF have provided to the United States in understanding the ecosystems of the Pacific region;\n**(3)**\nacknowledges the importance of having the IPIF located on Hawaii Island; and\n**(4)**\nreaffirms the Senate\u2019s strong support for the critical ongoing operations of the IPIF and its staff.",
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres742is.xml"
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
      "title": "A resolution commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T05:03:26Z"
    },
    {
      "title": "A resolution commemorating the 70th anniversary of the United States Forest Service Institute of Pacific Islands Forestry.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T10:56:30Z"
    }
  ]
}
```
