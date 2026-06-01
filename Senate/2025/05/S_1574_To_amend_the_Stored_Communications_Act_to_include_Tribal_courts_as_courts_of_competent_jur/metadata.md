# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1574?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1574
- Title: Tribal Access to Electronic Evidence Act
- Congress: 119
- Bill type: S
- Bill number: 1574
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-03T12:03:26Z
- Update date including text: 2026-03-03T12:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1574",
    "number": "1574",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Tribal Access to Electronic Evidence Act",
    "type": "S",
    "updateDate": "2026-03-03T12:03:26Z",
    "updateDateIncludingText": "2026-03-03T12:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-01",
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
            "date": "2025-05-01T17:29:44Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T17:29:44Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "SD"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "OK"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1574is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1574\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Ms. Cortez Masto (for herself and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Stored Communications Act to include Tribal courts as courts of competent jurisdiction.\n#### 1. Short title\nThis Act may be cited as the Tribal Access to Electronic Evidence Act .\n#### 2. Tribal courts as courts of competent jurisdiction under Stored Communications Act\n##### (a) Definitions\nSection 2711 of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (B), by striking or at the end;\n**(B)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(C)**\nby inserting after subparagraph (B) the following:\n(C) a Tribal court; or ; and\n**(2)**\nby striking paragraph (4) and inserting the following:\n(4) the term governmental entity means a department or agency of\u2014 (A) the United States; (B) any State or political subdivision thereof; or (C) any Indian Tribe or political subdivision thereof; (5) the term Indian Tribe means any Indian or Alaska Native tribe, band, nation, pueblo, village, community, component band, or component reservation individually identified (including parenthetically) on the most recent list published by the Secretary of the Interior under section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ); and (6) the term Tribal court means a court of general criminal jurisdiction of an Indian Tribe authorized by the law of that Indian Tribe to issue search warrants. .\n##### (b) Required disclosure of customer communications or records\nSection 2703 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by striking the first sentence and inserting the following:\n(1) In storage 180 days or less A governmental entity may require the disclosure by a provider of electronic communication service of the contents of a wire or electronic communication, that is in electronic storage in an electronic communications system for 180 days or less, only pursuant to a warrant issued by a court of competent jurisdiction\u2014 (A) issued using the procedures described in the Federal Rules of Criminal Procedure; (B) in the case of a State court, issued using State warrant procedures; (C) in the case of a court-martial or other proceeding under chapter 47 of title 10 (the Uniform Code of Military Justice), issued under section 846 of that title, in accordance with regulations prescribed by the President); or (D) in the case of a Tribal court, issued using the warrant procedures described in section 202(a)(2) of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1302(a)(2) ). (2) In storage more than 180 days ;\n**(2)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (A), by striking using the procedures described in the Federal Rules of Criminal Procedure and all that follows through prescribed by the President) and inserting in accordance with subsection (a)(1) ; and\n**(B)**\nin subparagraph (B)(i), by inserting , Tribal, after a Federal each place it appears; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by striking using the procedures described in the Federal Rules of Criminal Procedure and all that follows through prescribed by the President) and inserting in accordance with subsection (a)(1) ; and\n**(B)**\nin paragraph (2), in the undesignated matter following subparagraph (F), by inserting , Tribal, after a Federal each place it appears.\n##### (c) Delayed notice\nSection 2705(a)(1)(B) of title 18, United States Code, is amended by inserting , Tribal, after a Federal each place it appears.\n##### (d) Civil action\nSection 2707(g) of title 18, United States Code, is amended, in the second sentence, by inserting Tribal, after State, .\n##### (e) Wrongful disclosure of video tape rental or sale records\nSection 2710 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(2)(C), by inserting after an equivalent State warrant, the following: a warrant issued by a Tribal court using the warrant procedures described in section 202(a)(2) of Public Law 90\u2013284 (commonly known as the Indian Civil Rights Act of 1968 ) ( 25 U.S.C. 1302(a)(2) ), ; and\n**(2)**\nin subsection (d), by striking or a political subdivision of a State and inserting a political subdivision of a State, or an Indian Tribe .",
      "versionDate": "2025-05-01",
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
        "actionDate": "2025-06-05",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3773",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-05",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "1967",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PROTECT Act of 2025",
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
        "name": "Native Americans",
        "updateDate": "2025-06-03T18:20:50Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1574is.xml"
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
      "title": "Tribal Access to Electronic Evidence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T12:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Stored Communications Act to include Tribal courts as courts of competent jurisdiction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-15T03:59:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tribal Access to Electronic Evidence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-15T03:38:24Z"
    }
  ]
}
```
