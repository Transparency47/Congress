# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4448?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4448
- Title: Accelerating Broadband Permits Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4448
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-18T20:21:34Z
- Update date including text: 2026-05-18T20:21:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2173)
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2173)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4448",
    "number": "4448",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Accelerating Broadband Permits Act of 2026",
    "type": "S",
    "updateDate": "2026-05-18T20:21:34Z",
    "updateDateIncludingText": "2026-05-18T20:21:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S2173)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T16:33:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NM"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4448is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4448\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Thune (for himself, Mr. Luj\u00e1n , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Assistant Secretary of Commerce for Communications and Information to create tools for tracking the progress of grant recipients under the Broadband Equity, Access, and Deployment Program, to require the Assistant Secretary to help executive agencies improve compliance with the statutory deadline for processing communications use applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Broadband Permits Act of 2026 .\n#### 2. Tracking BEAD progress and permits\n##### (a) Progress dashboard\nSection 60102(j) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(j) ) is amended by adding at the end the following:\n(5) Progress dashboard The Assistant Secretary shall make available on a public website a dashboard that tracks the progress of each eligible entity through major milestones under the Program, including\u2014 (A) the amount of grant funds received under this section that the eligible entity has expended; and (B) the number of locations at which broadband service has been made available using grant funds received by the eligible entity under this section, and the number of those locations at which broadband service has been utilized. .\n##### (b) Tracking permits\nSection 60102(h) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(h) ) is amended\u2014\n**(1)**\nby redesignating paragraph (6) as paragraph (7); and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) Tracking permits The Assistant Secretary shall create a tool to help each eligible entity\u2014 (A) identify the relevant Federal permit requirements for each subgrantee of the eligible entity; and (B) monitor the progress of each subgrantee of the eligible entity toward obtaining Federal permits. .\n#### 3. Tracking and improving processing times for communications use applications\nSection 6409(b)(3) of the Middle Class Tax Relief and Job Creation Act of 2012 ( 47 U.S.C. 1455(b)(3) ) is amended by adding at the end the following:\n(E) Tracking and improving processing times (i) Data controls Not later than 90 days after the date of enactment of the Accelerating Broadband Permits Act of 2026 , the Assistant Secretary shall develop controls to ensure that data is sufficiently accurate and complete for an executive agency to track the processing time for each application described in subparagraph (A) received by the executive agency. (ii) Requirement to analyze, address, and report on delay factors With respect to the factors that contribute to delays in processing applications described in subparagraph (A), the Assistant Secretary shall\u2014 (I) analyze the factors as the delays are occurring; (II) take actions to address the factors; and (III) provide an annual report on the factors to\u2014 (aa) the Committee on Commerce, Science, and Transportation of the Senate; (bb) the Committee on Energy and Natural Resources of the Senate; (cc) the Committee on Energy and Commerce of the House of Representatives; and (dd) the Committee on Natural Resources of the House of Representatives. (iii) Method for alerting staff to at-risk applications Not later than 90 days after the date of enactment of the Accelerating Broadband Permits Act of 2026 , the Assistant Secretary shall establish a method to alert employees of an executive agency to any application described in subparagraph (A) with respect to which the executive agency is at risk of failing to meet the 270-day deadline under that subparagraph. .\n#### 4. Minimum broadband project cost\nSection 41001(6)(A) of the FAST Act ( 42 U.S.C. 4370m(6)(A) ) is amended\u2014\n**(1)**\nin clause (iii), by striking or at the end;\n**(2)**\nby redesignating clause (iv) as clause (v); and\n**(3)**\nby inserting after clause (iii) the following:\n(iv) (I) is subject to NEPA; (II) involves the construction of infrastructure for broadband; and (III) is likely to require a total investment of more than $5,000,000; or .",
      "versionDate": "2026-04-30",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-05-18T20:21:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4448is.xml"
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
      "title": "Accelerating Broadband Permits Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accelerating Broadband Permits Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Assistant Secretary of Commerce for Communications and Information to create tools for tracking the progress of grant recipients under the Broadband Equity, Access, and Deployment Program, to require the Assistant Secretary to help executive agencies improve compliance with the statutory deadline for processing communications use applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:32Z"
    }
  ]
}
```
