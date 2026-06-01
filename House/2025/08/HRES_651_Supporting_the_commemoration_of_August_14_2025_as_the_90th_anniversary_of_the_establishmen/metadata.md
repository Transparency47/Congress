# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/651
- Title: Supporting the commemoration of August 14, 2025, as the 90th anniversary of the establishment of Social Security.
- Congress: 119
- Bill type: HRES
- Bill number: 651
- Origin chamber: House
- Introduced date: 2025-08-15
- Update date: 2025-09-19T16:56:27Z
- Update date including text: 2025-09-19T16:56:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-15: Introduced in House
- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-08-15 - IntroReferral: Submitted in House
- 2025-08-15 - IntroReferral: Submitted in House
- Latest action: 2025-08-15: Submitted in House

## Actions

- 2025-08-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-08-15 - IntroReferral: Submitted in House
- 2025-08-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-15",
    "latestAction": {
      "actionDate": "2025-08-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/651",
    "number": "651",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001327",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
        "lastName": "Bresnahan",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Supporting the commemoration of August 14, 2025, as the 90th anniversary of the establishment of Social Security.",
    "type": "HRES",
    "updateDate": "2025-09-19T16:56:27Z",
    "updateDateIncludingText": "2025-09-19T16:56:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-15",
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
          "date": "2025-08-15T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "IA"
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
      "sponsorshipDate": "2025-08-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "CO"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres651ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 651\nIN THE HOUSE OF REPRESENTATIVES\nAugust 15, 2025 Mr. Bresnahan (for himself, Ms. Tenney , Mr. Lawler , Mr. Nunn of Iowa , Mrs. Kiggans of Virginia , Mr. Kean , and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Ways and Means\nRESOLUTION\nSupporting the commemoration of August 14, 2025, as the 90th anniversary of the establishment of Social Security.\nThat the House of Representatives supports the commemoration of the 90th anniversary of the Social Security Act ( 42 U.S.C. 301 et seq. ).",
      "versionDate": "2025-08-15",
      "versionType": "IH"
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
        "name": "Social Welfare",
        "updateDate": "2025-09-19T16:56:27Z"
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
      "date": "2025-08-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres651ih.xml"
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
      "title": "Supporting the commemoration of August 14, 2025, as the 90th anniversary of the establishment of Social Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-26T14:03:22Z"
    },
    {
      "title": "Supporting the commemoration of August 14, 2025, as the 90th anniversary of the establishment of Social Security.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-16T08:06:05Z"
    }
  ]
}
```
