# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1240?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1240
- Title: Expressing support for the designation of the week of May 8 through May 17, 2026, as "National American Birding Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1240
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-15T17:07:25Z
- Update date including text: 2026-05-15T17:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-30 - IntroReferral: Sponsor introductory remarks on measure. (CR E398)
- 2026-04-30 - IntroReferral: Submitted in House
- Latest action: 2026-04-30: Sponsor introductory remarks on measure. (CR E398)

## Actions

- 2026-04-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-30 - IntroReferral: Sponsor introductory remarks on measure. (CR E398)
- 2026-04-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Sponsor introductory remarks on measure. (CR E398)"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1240",
    "number": "1240",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "K000009",
        "district": "9",
        "firstName": "Marcy",
        "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
        "lastName": "Kaptur",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Expressing support for the designation of the week of May 8 through May 17, 2026, as \"National American Birding Week\".",
    "type": "HRES",
    "updateDate": "2026-05-15T17:07:25Z",
    "updateDateIncludingText": "2026-05-15T17:07:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
    },
    {
      "actionCode": "B00100",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E398)",
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
          "date": "2026-04-30T13:09:15Z",
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
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WI"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "IL"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1240ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1240\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Ms. Kaptur (for herself, Mr. Latta , Mr. Mrvan , Ms. Tlaib , and Mr. Wied ) submitted the following resolution; which was referred to the Committee on Natural Resources\nRESOLUTION\nExpressing support for the designation of the week of May 8 through May 17, 2026, as National American Birding Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National American Birding Week ;\n**(2)**\nrecognizes that birding is a pastime that generates billions in economic benefits annually;\n**(3)**\nunderstands that migratory bird populations face an array of natural and human-caused threats to their survival;\n**(4)**\napplauds coordinated efforts by Federal, State, and local governments, conservation organizations, and businesses to promote conservation of migratory birds and economic development through birding; and\n**(5)**\nencourages birders and the public at large to attend events such as the Biggest Week in American Birding to learn about bird migration and to support efforts by governments, conservation organizations, and businesses to preserve migratory bird populations.",
      "versionDate": "2026-04-30",
      "versionType": "IH"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-08",
        "text": "Sponsor introductory remarks on measure. (CR H1926)"
      },
      "number": "363",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of May 9 through May 18, 2025, as \"National American Birding Week\".",
      "type": "HRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2026-05-15T17:07:25Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1240ih.xml"
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
      "title": "Expressing support for the designation of the week of May 8 through May 17, 2026, as \"National American Birding Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T11:18:43Z"
    },
    {
      "title": "Expressing support for the designation of the week of May 8 through May 17, 2026, as \"National American Birding Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T08:08:02Z"
    }
  ]
}
```
