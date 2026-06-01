# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3082?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3082
- Title: American Shores Protection Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3082
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3082",
    "number": "3082",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "American Shores Protection Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-30T17:21:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:36Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "FL"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3082is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3082\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mrs. Moody (for herself, Mr. Scott of Florida , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit oil and natural gas exploration, development, and production in certain areas of the outer Continental Shelf off the coast of Florida, Georgia, and South Carolina, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Shores Protection Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that Congress supports the withdrawal of areas of the outer Continental Shelf described in the Presidential memorandum entitled Memorandum on Withdrawal of Certain Areas of the United States Outer Continental Shelf From Leasing Disposition and dated September 8, 2020.\n#### 3. Prohibition of oil and natural gas exploration, development, and production in certain areas of the outer Continental Shelf off the coast of Florida, Georgia, and South Carolina\nSection 8 of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1337 ) is amended by adding at the end the following:\n(q) Prohibition of oil and natural gas exploration, development, and production in certain areas off the coast of Florida, Georgia, and South Carolina (1) Prohibition Notwithstanding any other provision of this section or any other law, beginning on the date of enactment of this subsection and ending on June 30, 2032, the Secretary may not issue a lease or any other authorization for the exploration for, or development or production of, oil or natural gas in\u2014 (A) any area of the Eastern Gulf of Mexico that is referred to in section 104(a) of the Gulf of Mexico Energy Security Act of 2006 ( 43 U.S.C. 1331 note; Public Law 109\u2013432 ); (B) the South Atlantic Planning Area, as depicted in the 2024\u20132029 National Outer Continental Shelf Oil and Gas Leasing Proposed Final Program published on September 29, 2023, by the Bureau of Ocean Energy Management (as announced in the notice of availability of the Bureau of Ocean Energy Management entitled Notice of Availability of the 2024\u20132029 National Outer Continental Shelf Oil and Gas Leasing Proposed Final Program and Final Programmatic Environmental Impact Statement (88 Fed. Reg. 67798 (October 2, 2023))); or (C) the Straits of Florida Planning Area, as depicted in the 2024\u20132029 National Outer Continental Shelf Oil and Gas Leasing Proposed Final Program published on September 29, 2023, by the Bureau of Ocean Energy Management (as announced in the notice of availability of the Bureau of Ocean Energy Management entitled Notice of Availability of the 2024\u20132029 National Outer Continental Shelf Oil and Gas Leasing Proposed Final Program and Final Programmatic Environmental Impact Statement (88 Fed. Reg. 67798 (October 2, 2023))). (2) Limitation on effect Nothing in this subsection affects any right under any lease issued under this Act before the date of enactment of this subsection. .",
      "versionDate": "2025-10-30",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Florida",
            "updateDate": "2026-02-19T17:04:10Z"
          },
          {
            "name": "Georgia",
            "updateDate": "2026-02-19T17:04:17Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-02-19T17:04:31Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-02-19T17:04:40Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-02-19T17:04:45Z"
          },
          {
            "name": "South Carolina",
            "updateDate": "2026-02-19T17:01:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-11-25T20:21:35Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3082is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "American Shores Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Shores Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit oil and natural gas exploration, development, and production in certain areas of the outer Continental Shelf off the coast of Florida, Georgia, and South Carolina.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:21Z"
    }
  ]
}
```
