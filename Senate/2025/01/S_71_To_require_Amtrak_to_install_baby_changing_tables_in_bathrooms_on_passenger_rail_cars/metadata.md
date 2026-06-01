# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/71?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/71
- Title: Baby Changing on Board Act
- Congress: 119
- Bill type: S
- Bill number: 71
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2026-05-13T11:34:52Z
- Update date including text: 2026-05-13T11:34:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.
- 2026-04-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 378.
- 2026-05-11 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S2204; text: CR S2204)
- 2026-05-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-05-12 - Floor: Message on Senate action sent to the House.
- 2026-05-12 15:06:00 - Floor: Received in the House.
- 2026-05-12 15:11:30 - Floor: Held at the desk.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.
- 2026-04-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 378.
- 2026-05-11 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S2204; text: CR S2204)
- 2026-05-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-05-12 - Floor: Message on Senate action sent to the House.
- 2026-05-12 15:06:00 - Floor: Received in the House.
- 2026-05-12 15:11:30 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/71",
    "number": "71",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Baby Changing on Board Act",
    "type": "S",
    "updateDate": "2026-05-13T11:34:52Z",
    "updateDateIncludingText": "2026-05-13T11:34:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-12",
      "actionTime": "15:11:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-12",
      "actionTime": "15:06:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S2204; text: CR S2204)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 378.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-118.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-13",
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
            "date": "2026-04-22T17:06:11Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-12T15:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-13T22:21:14Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s71is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 71\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Welch (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require Amtrak to install baby changing tables in bathrooms on passenger rail cars.\n#### 1. Short title\nThis Act may be cited as the Baby Changing on Board Act .\n#### 2. Installation of baby changing tables on Amtrak trains\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by inserting after section 24313 the following:\n24314. Baby changing tables (a) Definitions In this section: (1) ADA-compliant restroom The term ADA-compliant restroom means a restroom that complies with the requirements set forth in section 242(a) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12162(a) ). (2) Baby changing table The term baby changing table means an elevated, freestanding structure generally designed to support and retain a child with a body weight of up to 30 pounds in a horizontal position for the purpose of allowing an individual to change the child\u2019s diaper, including pull-out or drop-down changing surfaces. (3) Covered passenger rail train The term covered passenger rail train \u2014 (A) means a passenger rail train that\u2014 (i) is owned and operated by the National Railroad Passenger Corporation (commonly known as Amtrak ); and (ii) was solicited for purchase after the date of the enactment of the Baby Changing on Board Act for use by Amtrak; and (B) does not include any passenger rail train that Amtrak operates, but does not own. (b) Baby changing tables (1) In general All covered passenger rail trains shall have a baby changing table in at least one restroom in each rail car, including in an ADA-compliant restroom. (2) Signage Such restroom shall clearly indicate with signage the presence of a baby changing table and such baby changing tables shall be clearly identified with signage. .\n##### (b) Clerical amendment\nThe chapter analysis for chapter 243 of title 49, United States Code, is amended by inserting after the item relating to section 24313 the following:\n24314. Baby changing tables. .",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s71rs.xml",
      "text": "II\nCalendar No. 378\n119th CONGRESS\n2d Session\nS. 71\n[Report No. 119\u2013118]\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Welch (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 22, 2026 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require Amtrak to install baby changing tables in bathrooms on passenger rail cars.\n#### 1. Short title\nThis Act may be cited as the Baby Changing on Board Act .\n#### 2. Installation of baby changing tables on Amtrak trains\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by inserting after section 24313 the following:\n24314. Baby changing tables (a) Definitions In this section: (1) ADA-compliant restroom The term ADA-compliant restroom means a restroom that complies with the requirements set forth in section 242(a) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12162(a) ). (2) Baby changing table The term baby changing table means an elevated, freestanding structure generally designed to support and retain a child with a body weight of up to 30 pounds in a horizontal position for the purpose of allowing an individual to change the child\u2019s diaper, including pull-out or drop-down changing surfaces. (3) Covered passenger rail train The term covered passenger rail train \u2014 (A) means a passenger rail train that\u2014 (i) is owned and operated by the National Railroad Passenger Corporation (commonly known as Amtrak ); and (ii) was solicited for purchase after the date of the enactment of the Baby Changing on Board Act for use by Amtrak; and (B) does not include any passenger rail train that Amtrak operates, but does not own. (b) Baby changing tables (1) In general All covered passenger rail trains shall have a baby changing table in at least one restroom in each rail car, including in an ADA-compliant restroom. (2) Signage Such restroom shall clearly indicate with signage the presence of a baby changing table and such baby changing tables shall be clearly identified with signage. .\n##### (b) Clerical amendment\nThe chapter analysis for chapter 243 of title 49, United States Code, is amended by inserting after the item relating to section 24313 the following:\n24314. Baby changing tables. .",
      "versionDate": "2026-04-22",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s71es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 71\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require Amtrak to install baby changing tables in bathrooms on passenger rail cars.\n#### 1. Short title\nThis Act may be cited as the Baby Changing on Board Act .\n#### 2. Installation of baby changing tables on Amtrak trains\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by inserting after section 24313 the following:\n24314. Baby changing tables (a) Definitions In this section: (1) ADA-compliant public restroom The term ADA-compliant public restroom means a restroom that is not in a private accommodation and complies with the requirements set forth in section 242(a) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12162(a) ). (2) Baby changing table The term baby changing table means an elevated structure generally designed to support and retain a child with a body weight of up to 30 pounds in a horizontal position for the purpose of allowing an individual to change the child\u2019s diaper, including pull-out or drop-down changing surfaces. (3) Covered passenger rail car The term covered passenger rail car \u2014 (A) means a passenger rail car that\u2014 (i) is owned and operated by\u2014 (I) the National Railroad Passenger Corporation (commonly known as Amtrak ); or (II) another intercity passenger rail service provider that\u2014 (aa) is the recipient or subrecipient of Federal financial assistance; or (bb) is a primary beneficiary of Federal financial assistance from a project for which another entity has received Federal financial assistance; (ii) is newly built and was solicited for purchase after the date of the enactment of the Baby Changing on Board Act ; and (iii) has at least one restroom that is not in a private accommodation; and (B) does not include\u2014 (i) a private rail car; or (ii) a historical or antiquated rail passenger car (as defined in section 304(c)(2) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12184(c)(2) )). (4) Private rail car The term private rail car means rail rolling equipment that is used only for excursion, recreational, or private transportation purposes. (b) Baby changing tables (1) In general All covered passenger rail cars shall have a baby changing table in at least one restroom, and when an ADA-compliant public restroom is present in the covered passenger car, such restroom shall have a baby changing table. (2) Signage Each restroom described in paragraph (1) shall clearly indicate with signage the presence of a baby changing table and such baby changing tables shall be clearly identified with signage. .\n##### (b) Clerical amendment\nThe chapter analysis for chapter 243 of title 49, United States Code, is amended by inserting after the item relating to section 24313 the following:\n24314. Baby changing tables. .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Child safety and welfare",
            "updateDate": "2025-04-16T17:09:38Z"
          },
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-04-16T17:09:38Z"
          },
          {
            "name": "National Railroad Passenger Corporation (Amtrak)",
            "updateDate": "2025-04-16T17:09:38Z"
          },
          {
            "name": "Railroads",
            "updateDate": "2025-04-16T17:09:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-12T18:54:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s71",
          "measure-number": "71",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s71v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Baby Changing on Board Act</strong></p><p>This bill requires Amtrak passenger rail trains to have a baby changing table in at least one restroom in each car,\u00a0including in an Americans with Disabilities Act of 1990-compliant\u00a0restroom.\u00a0The bill applies to passenger rail trains that are (1) owned and operated by Amtrak, and (2) solicited for purchase after the bill's enactment\u00a0for use by Amtrak.</p>"
        },
        "title": "Baby Changing on Board Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s71.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Baby Changing on Board Act</strong></p><p>This bill requires Amtrak passenger rail trains to have a baby changing table in at least one restroom in each car,\u00a0including in an Americans with Disabilities Act of 1990-compliant\u00a0restroom.\u00a0The bill applies to passenger rail trains that are (1) owned and operated by Amtrak, and (2) solicited for purchase after the bill's enactment\u00a0for use by Amtrak.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s71"
    },
    "title": "Baby Changing on Board Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Baby Changing on Board Act</strong></p><p>This bill requires Amtrak passenger rail trains to have a baby changing table in at least one restroom in each car,\u00a0including in an Americans with Disabilities Act of 1990-compliant\u00a0restroom.\u00a0The bill applies to passenger rail trains that are (1) owned and operated by Amtrak, and (2) solicited for purchase after the bill's enactment\u00a0for use by Amtrak.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s71"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s71is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s71rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s71es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Baby Changing on Board Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:31Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Baby Changing on Board Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-12T05:53:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Baby Changing on Board Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Baby Changing on Board Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Amtrak to install baby changing tables in bathrooms on passenger rail cars.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T03:03:28Z"
    }
  ]
}
```
