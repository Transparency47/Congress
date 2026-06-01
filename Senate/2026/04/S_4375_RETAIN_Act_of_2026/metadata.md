# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4375?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4375
- Title: RETAIN Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4375
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-13T20:49:15Z
- Update date including text: 2026-05-13T20:49:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-04-22: Introduced in Senate

## Actions

- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4375",
    "number": "4375",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "RETAIN Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T20:49:15Z",
    "updateDateIncludingText": "2026-05-13T20:49:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T18:44:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NH"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-22",
      "state": "ME"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MT"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "SD"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "ND"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4375is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4375\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Budd (for himself, Mrs. Shaheen , Mr. King , Mr. Schmitt , Mr. Sheehy , Mr. Rounds , Mr. Cramer , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 37, United States Code, to require the payment of the maximum amount of aviation incentive pay to aviation officers with more than 8 years of aviation service and to enhance the retention incentives available to aviation officers.\n#### 1. Short title\nThis Act may be cited as the Retention Enhancements for Tactical Aircrew INitiative Act of 2026 or the RETAIN Act of 2026 .\n#### 2. Payment of maximum amount of aviation incentive pay to officers with more than 8 years of aviation service\nSection 334(c) of title 37, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(A), by inserting subject to paragraph (5), before aviation incentive ; and\n**(2)**\nby adding at the end the following new paragraph:\n(5) Maximum amount for officers with more than 8 years of aviation service An officer who is entitled to aviation incentive pay under subsection (a) and has completed more than 8 years of aviation service shall receive the maximum monthly amount of such pay under paragraph (1)(A). .\n#### 3. Enhancement of Air Force rated officer retention demonstration program\n##### (a) Eligible officers\nSubsection (b)(2) of section 604 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ; 37 U.S.C. 301b note) is amended\u2014\n**(1)**\nby striking and not less than one year ; and\n**(2)**\nby striking under section 653 of title 10, United States Code .\n##### (b) Written agreements\nSubsection (c)(1) of such section is amended\u2014\n**(1)**\nby striking four years and inserting one year ; and\n**(2)**\nby striking under section 653 of title 10, United States Code .\n##### (c) Retention incentives\nSubsection (d) of such section is amended\u2014\n**(1)**\nby striking paragraph (1) and inserting the following new paragraph (1):\n(1) Flexibility of assignment and duty locations Under the demonstration program required under subsection (a), the Secretary shall offer to a rated officer described in subsection (b), to the maximum extent practicable (as determined by the Secretary)\u2014 (A) assignment to the duty location of the rated officer\u2019s preference, including consecutive assignments to the same duty location; (B) the opportunity to perform a staff assignment that does not require flying remotely, such that the officer may avoid relocation or remain in active flying status; and (C) the opportunity to transition indefinitely to a non-combat aviation service position. ;\n**(2)**\nby striking paragraph (2) and inserting the following new paragraph (2):\n(2) Aviation bonus (A) In general Under the demonstration program required under subsection (a), notwithstanding section 334(c) of title 37, United States Code, the Secretary may pay to a rated officer described in subsection (b) an aviation bonus not to exceed an average annual amount of $100,000. (B) Payment of maximum amount The Secretary\u2014 (i) shall ensure the maximum amount payable under subparagraph (A) is offered to any rated officer described in subsection (b) who executes a written agreement under subsection (c) to remain on active duty for one or more years after the completion of the active duty service obligation of the officer; and (ii) may not vary the amount of an aviation bonus offered to an officer based on the active duty service commitment the officer has remaining at the time of offer. ; and\n**(3)**\nby adding at the end the following new paragraph:\n(4) Aligning total force incentives The Secretary shall ensure that an offer under this subsection to a rated officer described in subsection (b) includes\u2014 (A) contract length options equal to or shorter than contract length options offered by the Air National Guard and the Air Force Reserve; and (B) an aviation bonus under paragraph (2) in an amount that is equal to or exceeds the amounts offered by the Air National Guard and the Air Force Reserve. .\n##### (d) Extension of demonstration project\nSubsection (g) of such section is amended by striking 2028 and inserting 2031 .",
      "versionDate": "2026-04-22",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-13T20:49:15Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4375is.xml"
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
      "title": "RETAIN Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RETAIN Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retention Enhancements for Tactical Aircrew INitiative Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 37, United States Code, to require the payment of the maximum amount of aviation incentive pay to aviation officers with more than 8 years of aviation service and to enhance the retention incentives available to aviation officers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:35Z"
    }
  ]
}
```
