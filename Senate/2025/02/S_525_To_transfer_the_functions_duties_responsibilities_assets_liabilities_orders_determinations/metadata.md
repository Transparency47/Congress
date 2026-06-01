# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/525
- Title: A bill to transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.
- Congress: 119
- Bill type: S
- Bill number: 525
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-03-17T10:56:21Z
- Update date including text: 2026-03-17T10:56:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/525",
    "number": "525",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A bill to transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.",
    "type": "S",
    "updateDate": "2026-03-17T10:56:21Z",
    "updateDateIncludingText": "2026-03-17T10:56:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
        "item": [
          {
            "date": "2025-02-11T20:54:22Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-11T20:54:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "LA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "TN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "MS"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "LA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "MS"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s525is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 525\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Moran (for himself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.\n#### 1. Transfer of functions\n##### (a) In general\nBeginning on the date of enactment of this Act, the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the Administrator of the United States Agency for International Development relating to carrying out any authority under the Food for Peace Act ( 7 U.S.C. 1691 et seq. ) shall be transferred to the Secretary of Agriculture.\n##### (b) References\nAny reference in any provision of law or regulation to the Administrator or Agency referred to in subsection (a), as applicable, shall be deemed to be a reference to the Secretary of Agriculture or to any department or office of the Department of Agriculture to which the Secretary assigns the functions, duties, or responsibilities transferred pursuant to this Act, respectively.\n##### (c) Regulations\nNotwithstanding any other provision of law, the Secretary of Agriculture may implement amendments to a regulation referred to in subsection (a), which shall be published as an interim final rule and may be made effective immediately on publication, to ensure continuity of the applicable program as a result of a transfer under this Act.\n##### (d) Authorities\nAny existing statutory authorities available to the Administrator of the United States Agency for International Development that have or could have been used by the Administrator to implement the functions, duties, or responsibilities of the United States Agency for International Development relating to implementing or administering the Food for Peace Act ( 7 U.S.C. 1691 et seq. ) may be exercised by the Secretary of Agriculture.\n##### (e) Famine Early Warning Systems Network\nNotwithstanding subsection (a), the Secretary of Agriculture shall continue to carry out the Famine Early Warning Systems Network or a successor program, 1 of the purposes of which is to provide objective, evidence-based analyses with respect to potential or existing famine and flood situations to assist the Secretary of Agriculture in mitigating food insecurity.\n##### (f) Consultation\nThe Secretary of Agriculture shall consult with the Secretary of State from time to time in carrying out the authorities under title II of the Food for Peace Act ( 7 U.S.C. 1721 et seq. ).",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-11",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.",
      "type": "HR"
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
        "name": "International Affairs",
        "updateDate": "2025-05-07T14:25:10Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s525is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:14Z"
    },
    {
      "title": "A bill to transfer the functions, duties, responsibilities, assets, liabilities, orders, determinations, rules, regulations, permits, grants, loans, contracts, agreements, certificates, licenses, and privileges of the United States Agency for International Development relating to implementing and administering the Food for Peace Act to the Department of Agriculture.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T11:56:19Z"
    }
  ]
}
```
