# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1110
- Title: Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1110
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-02-10T00:09:28Z
- Update date including text: 2026-02-10T00:09:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1110",
    "number": "1110",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T00:09:28Z",
    "updateDateIncludingText": "2026-02-10T00:09:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T16:08:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "NE"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1110is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1110\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Husted (for himself, Ms. Ernst , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the use of artificial intelligence to review agency regulations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(2) Artificial intelligence system**\nThe term artificial intelligence system means a machine-based system that, for an explicit or implicit objective, infers how to generate outputs, such as predictions, content, recommendations, or decisions that can influence physical or virtual environments, from the input the system receives.\n**(3) Redundant**\nThe term redundant means a regulation that duplicates, overlaps with, or serves the same purpose as another regulation, such that the elimination of the regulation would not result in a loss of essential information or regulatory function.\n**(4) Regulation**\nThe term regulation has the meaning given the term rule in section 551 of title 5, United States Code.\n**(5) Outdated**\nThe term outdated means a regulation that has been superseded by more recent legislation, technological advances, or regulatory developments, rendering the regulation inapplicable or unenforceable.\n#### 3. Annual artificial intelligence review of the code of federal regulations\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, and annually thereafter, the Director of the Office of Management and Budget, in consultation with the National Institute of Standards and Technology, shall implement a process for identifying redundant or outdated regulations in the Code of Federal Regulations using an artificial intelligence system.\n##### (b) Artificial intelligence system\nThe process established under subsection (a) shall employ an artificial intelligence system that meets strict standards, as set out by the National Institute of Standards and Technology, for accuracy, transparency, accountability, and national security risk.\n##### (c) Review of process and artificial intelligence system\nNot less frequently than once per fiscal year, the Director of the Office of Management and Budget, in coordination with the head of the National Institute of Standards and Technology, shall review and, as appropriate, revise the process established under subsection (a) to ensure that\u2014\n**(1)**\nthe process is functioning properly and efficiently; and\n**(2)**\nthe underlying artificial intelligence system involved in such process still meets the criteria under subsection (b).\n##### (d) Review of regulations\n**(1) Referral and review**\nA regulation that is identified as redundant or outdated using the process established under subsection (a) shall be immediately referred to the agency responsible for promulgating the regulation for review by that agency.\n**(2) Determination**\n**(A) In general**\nNot later than 30 days after a regulation is referred to an agency under paragraph (1), personnel at that agency shall make a determination as to whether the regulation is outdated or redundant.\n**(B) Finality of determination**\nAny determination made under subparagraph (A) shall be final.\n##### (e) Rescission of regulations\nNot later than 30 days after the date on which a regulation has been determined to be redundant under subsection (d), the agency that promulgated the regulation shall rescind or remove such regulation from the Code of Federal Regulations, notwithstanding the requirements under subchapter II of chapter 5 of title 5, United States Code.\n##### (f) Amendment of regulations\nNot later than 30 days after the date on which a regulation has been determined to be outdated under subsection (d), the agency that promulgated the regulation shall\u2014\n**(1)**\namend the regulation, notwithstanding the requirements under subchapter II of chapter 5 of title 5, United States Code, for the purposes of bringing the outdated substance up to date; or\n**(2)**\nrescind or remove such regulation from the Code of Federal Regulations, notwithstanding the requirements under subchapter II of chapter 5 of title 5, United States Code.\n##### (g) Written determination\n**(1) In general**\nAny determination made under subsection (d) shall be immediately published on the website of the relevant agency, including a brief written explanation of the determination, which shall be made publicly available.\n**(2) Classified annex**\nThe head of the agency may, as necessary, submit a classified annex to Congress to supplement the explanation published under subsection (g).\n#### 4. Expedited rescission and amendment of redundant and outdated regulations\nSection 553(b) of title 5, United States Code, is amended in the flush text at the end\u2014\n**(1)**\nin subparagraph (A), by striking or at the end;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(C) a regulation determined to be redundant or outdated as part of the annual review of the Code of Federal Regulations under the Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025. .",
      "versionDate": "2025-03-25",
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
        "actionDate": "2026-01-22",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7226",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2026",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T14:32:35Z"
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
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1110is.xml"
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
      "title": "Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the use of artificial intelligence to review agency regulations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:16Z"
    }
  ]
}
```
