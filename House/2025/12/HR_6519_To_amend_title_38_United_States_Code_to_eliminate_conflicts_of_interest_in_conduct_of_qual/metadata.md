# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6519?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6519
- Title: Veterans Affairs Peer Review Neutrality Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6519
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-01-09T18:05:28Z
- Update date including text: 2026-01-09T18:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6519",
    "number": "6519",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Veterans Affairs Peer Review Neutrality Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T18:05:28Z",
    "updateDateIncludingText": "2026-01-09T18:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:14:26Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6519ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6519\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mrs. Dingell (for herself and Mr. Bergman ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to eliminate conflicts of interest in conduct of quality management and administrative investigations by the Veterans Health Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Peer Review Neutrality Act of 2025 .\n#### 2. Elimination of conflicts of interest in peer review, administrative investigation boards, and factfindings of Veterans Health Administration\n##### (a) In general\nSubchapter II of chapter 73 of title 38, United States Code, is amended by inserting after section 7311A the following new section:\n7311B. Elimination of conflicts of interest in peer review, administrative investigation boards, and factfindings of Veterans Health Administration (a) Peer review (1) In general Each individual responsible for conducting peer review for quality management of care provided by a health care provider at a medical facility of the Department and each member of a peer review committee with respect to quality management of such care shall withdraw from participation in a case review if\u2014 (A) the individual has direct involvement with the care under review; or (B) the individual is unable to conduct an objective, impartial, accurate, and informed review. (2) Neutral assessment of conduct of committee members Each medical facility of the Department shall develop procedures and guidelines for that facility to require that any initial peer review for quality management that is conducted with respect to care provided by a health care provider who is a member of the peer review committee for that facility be evaluated, discussed, and assigned a final level review by a neutral peer review committee at another facility of the Department. (b) Administrative investigation boards and factfindings (1) Knowledge of confidential information Individuals with knowledge of confidential quality assurance information specific to a matter under investigation by an administrative investigation board or factfinder with respect to quality management of care provided by a health care provider at a medical facility of the Department may not\u2014 (A) serve on the administrative investigation board or as a factfinder; or (B) disclose such information to an administrative investigation board or a factfinder. (2) Personal interest, involvement, or relationship (A) In general The Secretary shall ensure that each member of an administrative investigative board or factfinder does not have\u2014 (i) any personal interest or other bias concerning the investigation being conducted; (ii) direct involvement in matters being investigated; or (iii) a supervisory or personal relationship with the subject of the investigation. (B) Recusal If a potential member of an administrative investigative board or factfinder has a personal interest or other bias concerning the investigation being conducted, direct involvement in matters being investigated, or a supervisory or personal relationship with the subject of the investigation, the potential member shall inform the authority responsible for the investigation and recuse themselves from such matter. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such subchapter is amended by inserting after the item relating to section 7311A the following new item:\n7311B. Elimination of conflicts of interest in peer review, administrative investigation boards, and factfindings of Veterans Health Administration. .",
      "versionDate": "2025-12-09",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3311",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans Affairs Peer Review Neutrality Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:47:33Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6519ih.xml"
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
      "title": "Veterans Affairs Peer Review Neutrality Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-27T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Affairs Peer Review Neutrality Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-27T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to eliminate conflicts of interest in conduct of quality management and administrative investigations by the Veterans Health Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:17Z"
    }
  ]
}
```
