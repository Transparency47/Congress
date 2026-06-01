# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1264
- Title: Supporting the goals and ideals of "National Nurses Week", to be observed from May 6 through May 12, 2026.
- Congress: 119
- Bill type: HRES
- Bill number: 1264
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T14:54:15Z
- Update date including text: 2026-05-21T14:54:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-07 - IntroReferral: Submitted in House
- Latest action: 2026-05-07: Submitted in House

## Actions

- 2026-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1264",
    "number": "1264",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000295",
        "district": "14",
        "firstName": "David",
        "fullName": "Rep. Joyce, David P. [R-OH-14]",
        "lastName": "Joyce",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Supporting the goals and ideals of \"National Nurses Week\", to be observed from May 6 through May 12, 2026.",
    "type": "HRES",
    "updateDate": "2026-05-21T14:54:15Z",
    "updateDateIncludingText": "2026-05-21T14:54:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
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
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:07:15Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "OR"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1264ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1264\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Joyce of Ohio (for himself, Ms. Bonamici , Mrs. Kiggans of Virginia , and Ms. Underwood ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of National Nurses Week , to be observed from May 6 through May 12, 2026.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of National Nurses Week , as founded by the American Nurses Association;\n**(2)**\nrecognizes the significant contributions of nurses to the health care system of the United States; and\n**(3)**\nencourages the people of the United States to observe National Nurses Week with appropriate recognition, ceremonies, activities, and programs to demonstrate the importance of nurses to the everyday lives of patients.",
      "versionDate": "2026-05-07",
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
        "actionDate": "2026-04-30",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2175)"
      },
      "number": "709",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2026.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "389",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2778)"
      },
      "number": "206",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of National Nurses Week, to be observed from May 6 through May 12, 2025.",
      "type": "SRES"
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
        "name": "Health",
        "updateDate": "2026-05-21T14:54:14Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1264ih.xml"
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
      "title": "Supporting the goals and ideals of \"National Nurses Week\", to be observed from May 6 through May 12, 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T08:18:38Z"
    },
    {
      "title": "Supporting the goals and ideals of \"National Nurses Week\", to be observed from May 6 through May 12, 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T08:06:53Z"
    }
  ]
}
```
