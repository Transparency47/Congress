# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/28?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/28
- Title: Informing Consumers about Smart Devices Act
- Congress: 119
- Bill type: S
- Bill number: 28
- Origin chamber: Senate
- Introduced date: 2025-01-07
- Update date: 2026-03-24T11:03:18Z
- Update date including text: 2026-03-24T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in Senate
- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 47.
- Latest action: 2025-01-07: Introduced in Senate

## Actions

- 2025-01-07 - IntroReferral: Introduced in Senate
- 2025-01-07 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 47.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/28",
    "number": "28",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Informing Consumers about Smart Devices Act",
    "type": "S",
    "updateDate": "2026-03-24T11:03:18Z",
    "updateDateIncludingText": "2026-03-24T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 47.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-13.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
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
            "date": "2025-04-28T20:14:44Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-07T19:31:40Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-01-07",
      "state": "WA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "UT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s28is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 28\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Cruz (for himself, Ms. Cantwell , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the disclosure of a camera or recording capability in certain internet-connected devices.\n#### 1. Short title\nThis Act may be cited as the Informing Consumers about Smart Devices Act .\n#### 2. Required disclosure of a camera or recording capability in certain internet-connected devices\nEach manufacturer of a covered device shall disclose, clearly and conspicuously and prior to purchase, whether the covered device manufactured by the manufacturer contains a camera or microphone as a component of the covered device.\n#### 3. Enforcement by the Federal Trade Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of section 2 shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Actions by the Commission\n**(1) In general**\nThe Federal Trade Commission (in this Act referred to as the Commission ) shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Penalties and privileges**\nAny person who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Savings clause**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Commission guidance\nNot later than 180 days after the date of enactment of this Act, the Commission, through outreach to relevant private entities, shall issue guidance to assist manufacturers in complying with the requirements of this Act, including guidance about best practices for making the disclosure required by section 2 as clear and conspicuous and age appropriate as practicable and about best practices for the use of a pictorial (as defined in section 2(a) of the Consumer Review Fairness Act of 2016 ( 15 U.S.C. 45b(a) )) visual representation of the information to be disclosed.\n##### (d) Tailored guidance\nA manufacturer of a covered device may petition the Commission for tailored guidance as to how to meet the requirements of section 2 consistent with existing rules of practice or any successor rules.\n##### (e) Limitation on Commission Guidance\nNo guidance issued by the Commission with respect to this Act shall confer any rights on any person, State, or locality, nor shall operate to bind the Commission or any person to the approach recommended in such guidance. In any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act. The Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any such guidelines, unless the practices allegedly violate section 2.\n#### 4. Definition of covered device\nAs used in this Act, the term covered device \u2014\n**(1)**\nmeans a consumer product, as defined by section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ) that is capable of connecting to the internet, a component of which is a camera or microphone; and\n**(2)**\ndoes not include\u2014\n**(A)**\na telephone (including a mobile phone), a laptop, tablet, or any device that a consumer would reasonably expect to have a microphone or camera;\n**(B)**\nany device that is specifically marketed as a camera, telecommunications device, or microphone; or\n**(C)**\nany device or apparatus described in sections 255, 716, and 718, and subsections (aa) and (bb) of section 303 of the Communications Act of 1934 ( 47 U.S.C. 255 ; 617; 619; and 303(aa) and (bb)), and any regulations promulgated thereunder.\n#### 5. Effective date\nThis Act shall apply to all covered devices manufactured after the date that is 180 days after the date on which guidance is issued by the Commission under section 3(c), and shall not apply to covered devices manufactured or sold before such date, or otherwise introduced into interstate commerce before such date.",
      "versionDate": "2025-01-07",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s28rs.xml",
      "text": "II\nCalendar No. 47\n119th CONGRESS\n1st Session\nS. 28\nReport No. 119\u201313]\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2025 Mr. Cruz (for himself, Ms. Cantwell , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 28, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo require the disclosure of a camera or recording capability in certain internet-connected devices.\n#### 1. Short title\nThis Act may be cited as the Informing Consumers about Smart Devices Act .\n#### 2. Required disclosure of a camera or recording capability in certain internet-connected devices\nEach manufacturer of a covered device shall disclose, clearly and conspicuously and prior to purchase, whether the covered device manufactured by the manufacturer contains a camera or microphone as a component of the covered device.\n#### 3. Enforcement by the Federal Trade Commission\n##### (a) Unfair or deceptive acts or practices\nA violation of section 2 shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Actions by the Commission\n**(1) In general**\nThe Federal Trade Commission (in this Act referred to as the Commission ) shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Penalties and privileges**\nAny person who violates this Act or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Savings clause**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Commission guidance\nNot later than 180 days after the date of enactment of this Act, the Commission, through outreach to relevant private entities, shall issue guidance to assist manufacturers in complying with the requirements of this Act, including guidance about best practices for making the disclosure required by section 2 as clear and conspicuous and age appropriate as practicable and about best practices for the use of a pictorial (as defined in section 2(a) of the Consumer Review Fairness Act of 2016 ( 15 U.S.C. 45b(a) )) visual representation of the information to be disclosed.\n##### (d) Tailored guidance\nA manufacturer of a covered device may petition the Commission for tailored guidance as to how to meet the requirements of section 2 consistent with existing rules of practice or any successor rules.\n##### (e) Limitation on Commission Guidance\nNo guidance issued by the Commission with respect to this Act shall confer any rights on any person, State, or locality, nor shall operate to bind the Commission or any person to the approach recommended in such guidance. In any enforcement action brought pursuant to this Act, the Commission shall allege a specific violation of a provision of this Act. The Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any such guidelines, unless the practices allegedly violate section 2.\n#### 4. Definition of covered device\nAs used in this Act, the term covered device \u2014\n**(1)**\nmeans a consumer product, as defined by section 3(a) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a) ) that is capable of connecting to the internet, a component of which is a camera or microphone; and\n**(2)**\ndoes not include\u2014\n**(A)**\na telephone (including a mobile phone), a laptop, tablet, or any device that a consumer would reasonably expect to have a microphone or camera;\n**(B)**\nany device that is specifically marketed as a camera, telecommunications device, or microphone; or\n**(C)**\nany device or apparatus described in sections 255, 716, and 718, and subsections (aa) and (bb) of section 303 of the Communications Act of 1934 ( 47 U.S.C. 255 ; 617; 619; and 303(aa) and (bb)), and any regulations promulgated thereunder.\n#### 5. Effective date\nThis Act shall apply to all covered devices manufactured after the date that is 180 days after the date on which guidance is issued by the Commission under section 3(c), and shall not apply to covered devices manufactured or sold before such date, or otherwise introduced into interstate commerce before such date.",
      "versionDate": "2025-04-28",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-03-13T14:45:56Z"
          },
          {
            "name": "Sound recording",
            "updateDate": "2025-03-13T14:45:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-18T14:29:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119s28",
          "measure-number": "28",
          "measure-type": "s",
          "orig-publish-date": "2025-01-07",
          "originChamber": "SENATE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s28v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Informing Consumers about Smart Devices Act</strong></p> <p>This bill requires manufacturers of internet-connected devices (e.g., smart appliances) that are equipped with a camera or microphone to disclose to consumers prior to purchase that a camera or microphone is part of the device.</p> <p>The bill does not apply to mobile phones, laptops, or other devices that a consumer would reasonably expect to include a camera or microphone.</p>"
        },
        "title": "Informing Consumers about Smart Devices Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s28.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Informing Consumers about Smart Devices Act</strong></p> <p>This bill requires manufacturers of internet-connected devices (e.g., smart appliances) that are equipped with a camera or microphone to disclose to consumers prior to purchase that a camera or microphone is part of the device.</p> <p>The bill does not apply to mobile phones, laptops, or other devices that a consumer would reasonably expect to include a camera or microphone.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119s28"
    },
    "title": "Informing Consumers about Smart Devices Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Informing Consumers about Smart Devices Act</strong></p> <p>This bill requires manufacturers of internet-connected devices (e.g., smart appliances) that are equipped with a camera or microphone to disclose to consumers prior to purchase that a camera or microphone is part of the device.</p> <p>The bill does not apply to mobile phones, laptops, or other devices that a consumer would reasonably expect to include a camera or microphone.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119s28"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s28is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s28rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Informing Consumers about Smart Devices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Informing Consumers about Smart Devices Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Informing Consumers about Smart Devices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the disclosure of a camera or recording capability in certain internet-connected devices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:27Z"
    }
  ]
}
```
