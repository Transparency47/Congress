# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7409
- Title: Defend Rural Health Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7409
- Origin chamber: House
- Introduced date: 2026-02-05
- Update date: 2026-05-13T08:06:06Z
- Update date including text: 2026-05-13T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-05: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-05: Introduced in House

## Actions

- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Introduced in House
- 2026-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-05",
    "latestAction": {
      "actionDate": "2026-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7409",
    "number": "7409",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Defend Rural Health Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:06Z",
    "updateDateIncludingText": "2026-05-13T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-05",
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
      "actionCode": "Intro-H",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-02-05T15:01:30Z",
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
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "WV"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "KS"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "MI"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NE"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NE"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7409ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7409\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2026 Mr. Taylor (for himself and Mrs. Miller of West Virginia ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to limit the geographic reclassification of certain hospitals under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Defend Rural Health Act of 2026 .\n#### 2. Limiting geographic reclassification of hospitals under Medicare\n##### (a) In general\nSection 1886(d)(8)(E) of the Social Security Act ( 42 U.S.C. 1395ww(d)(8)(E) ) is amended\u2014\n**(1)**\nin clause (i), by striking described in clause (ii) and inserting that is located in an urban area (as defined in paragraph (2)(D)) and meets any of the criteria described in subclause (I), (II), or (IV) of clause (ii) (or, with respect to a hospital submitting such an application before October 1, 2026, meets any of the criteria described in such clause) ;\n**(2)**\nin clause (ii)\u2014\n**(A)**\nin the matter preceding subclause (I), by striking a subsection (d) hospital and all that follows through criteria: and inserting the criteria described in this clause are the following: ; and\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby inserting that is before designated by any law ; and\n**(ii)**\nby inserting , and that was so designated as of January 1, 2026 before the period at the end; and\n**(3)**\nby adding at the end the following new clause:\n(iii) No subsection (d) hospital shall be treated as being located in a rural area of a State under this subparagraph on or after October 1, 2029, regardless of any application described in clause (i) submitted prior to October 1, 2026, unless such hospital demonstrates to the Secretary (in a form and manner specified by the Secretary) that such hospital meets any of the criteria described in subclause (I), (II), or (IV) of clause (ii). .\n##### (b) Prohibiting dual reclassifications through the Medicare Geographic Classification Review Board\nSection 1886(d)(10)(D) of the Social Security Act ( 42 U.S.C. 1395ww(d)(10)(D) ) is amended\u2014\n**(1)**\nin clause (v), by striking Any decision and inserting Subject to clause (viii), any decision ; and\n**(2)**\nby adding at the end the following new clauses:\n(vii) Such guidelines shall provide that the Board may not approve an application described in subparagraph (C)(i) submitted by a subsection (d) hospital requesting a change in geographic classification for a fiscal year beginning on or after October 1, 2026, if such hospital is treated as being located in a rural area under paragraph (8)(E) for such fiscal year. (viii) With respect to a fiscal year beginning on or after October 1, 2026, no change in the geographic classification of a subsection (d) hospital that would otherwise be in effect for such fiscal year pursuant to a decision of the Board shall be effective for any portion of such fiscal year during which such hospital is treated as being located in a rural area under paragraph (8)(E). .",
      "versionDate": "2026-02-05",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-26T18:21:25Z"
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
      "date": "2026-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7409ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Defend Rural Health Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defend Rural Health Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to limit the geographic reclassification of certain hospitals under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:32Z"
    }
  ]
}
```
