# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4033
- Title: Sturgeon Conservation and Sustainability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4033
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-04-14T08:05:44Z
- Update date including text: 2026-04-14T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-16 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-07-22 - Committee: Subcommittee Hearings Held
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-16 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-07-22 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4033",
    "number": "4033",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Sturgeon Conservation and Sustainability Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:44Z",
    "updateDateIncludingText": "2026-04-14T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-07-22T18:29:36Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-07-16T15:10:35Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "UT"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "NC"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4033ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4033\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Fine introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to allow certain activities to be conducted with respect to sturgeon held in captivity or in a controlled environment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sturgeon Conservation and Sustainability Act of 2025 .\n#### 2. Sturgeon held in captivity or controlled environments\nSection 9(b) of the Endangered Species Act of 1973 ( 16 U.S.C. 1538(b) ) is amended by adding at the end the following:\n(3) Sturgeon (A) In general Subsection (a)(1) and section 7(a)(2) shall not apply to\u2014 (i) a sturgeon farmed that is legally held in captivity or in a controlled environment as of the date of enactment of this paragraph, until such time as the sturgeon is intentionally returned to a wild state; or (ii) progeny of a sturgeon described in clause (i), until such time as the progeny is intentionally returned to a wild state. (B) Demonstration; requirements (i) In general Any person holding any sturgeon or progeny described in subparagraph (A) shall\u2014 (I) be able to demonstrate that the sturgeon or progeny qualifies as a sturgeon or progeny, as applicable, described in that subparagraph; and (II) maintain and submit to the Secretary, on request of the Secretary, such inventories, documentation, and records as the Secretary may, by regulation, require as being reasonably appropriate to carry out the purposes of this paragraph. (ii) Requirements Requirements described in clause (i)(II) shall not unnecessarily duplicate the requirements of other rules and regulations promulgated by the Secretary under this Act. .",
      "versionDate": "2025-06-17",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-17",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "2089",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Sturgeon Conservation and Sustainability Act",
      "type": "S"
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
            "name": "Aquaculture",
            "updateDate": "2025-08-27T17:17:50Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-08-27T17:17:50Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2025-08-27T17:17:50Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2025-08-27T17:17:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-07-08T12:54:33Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4033ih.xml"
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
      "title": "Sturgeon Conservation and Sustainability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sturgeon Conservation and Sustainability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to allow certain activities to be conducted with respect to sturgeon held in captivity or in a controlled environment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T07:18:35Z"
    }
  ]
}
```
