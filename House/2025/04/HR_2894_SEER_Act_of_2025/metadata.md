# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2894?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2894
- Title: SEER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2894
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-01-14T05:05:16Z
- Update date including text: 2026-01-14T05:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2894",
    "number": "2894",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001218",
        "district": "1",
        "firstName": "Melanie",
        "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
        "lastName": "Stansbury",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "SEER Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T05:05:16Z",
    "updateDateIncludingText": "2026-01-14T05:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:11:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:11:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "DC"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2894ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2894\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Ms. Stansbury (for herself, Ms. Norton , Mr. Lynch , Ms. McCollum , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 18, United States Code, to modify the definition of special Government employee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SGE Ethics Enforcement Reform Act of 2025 or the SEER Act of 2025\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSome special Government employees have substantial financial conflicts of interest due to their other business activities while in Federal service.\n**(2)**\nSpecial Government employees are subject to the criminal conflict-of-interest statute applicable to full-time Government employees, section 208 of title 18, United States Code. However, Federal employees, including special Government employees, do not have to resolve conflicts under that provision if the relevant work does not constitute a particular matter.\n**(3)**\nUnlike senior executive branch employees under chapter 131 of title 5, United States Code, the vast majority of special Government employees are not required to make their financial disclosure reports public, thus concealing from the public their potential financial conflicts of interest.\n**(4)**\nThe vast majority of special Government employees in the Federal Government serve on advisory committees and have a limited role in Government decision-making. But a select number of special Government employees have assumed authority within the Federal Government commensurate with a senior or very senior full-time Federal employee.\n**(5)**\nThe executive branch has not notified the public or Congress when it uses special Government employees to perform high-level responsibilities.\n**(6)**\nThe executive branch has permitted employees to retain special Government employee status beyond the statutory limit of 130 days during any period of 365 consecutive days.\n#### 3. Conflicts of interest\nTitle 18, United States Code, is amended\u2014\n**(1)**\nin section 202(a), in the first sentence, by inserting and who has been designated as a special Government employee on a Notification of Personnel Action (Standard Form 50 or equivalent) of the officer or employee, after basis, ; and\n**(2)**\nin section 208\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (a) Except and inserting (a)(1) Except ; and\n**(ii)**\nby adding at the end the following:\n(2) In the case of a special Government employee who is not on an advisory committee or who serves as the chair or vice chair of an advisory committee, paragraph (1) shall apply to a discrete and identifiable component of a matter that on its own would constitute a particular matter in which, to the knowledge of the special Government employee, the organization in which the special Government employee is serving as officer, director, trustee, general partner, or employee has a financial interest. ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by inserting , with the concurrence of a designated official at the Office of Government Ethics if the officer or employee is a special Government employee, after such official ; and\n**(ii)**\nin paragraph (3), by inserting , other than the chair or vice chair of the committee, after committee ;\n**(C)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1), in the first sentence, by striking Upon and inserting Except as provided in paragraph (2), upon ;\n**(ii)**\nby redesignating paragraph (2) as paragraph (3); and\n**(iii)**\nby inserting after paragraph (1) the following:\n(2) In the case of a special Government employee who is not serving on an advisory committee within the meaning of chapter 10 of title 5 or a special Government employee who is serving as chair or vice chair on such an advisory committee, any waiver or exemption granted under subsection (b)(1) shall be proactively made publicly available via a searchable online database not later than 14 days after the date on which the waiver is issued. .\n#### 4. Restriction on communications with agencies\n##### (a) Definition\nIn this section, the term large company means\u2014\n**(1)**\nany for-profit company that has greater than an average of $1,000,000,000 in market capitalization or revenue for the previous 3-year period;\n**(2)**\nany Federal contractor that received greater than $100,000,000 in annual revenue from the Federal Government during the previous 3-year period; and\n**(3)**\nany for-profit company that exerts monopolistic or monopsonistic control over a significant share of the market in its particular industry, as defined by regulation by the Director of the Office of Government Ethics, in consultation with the Attorney General.\n##### (b) Restriction\nNo special Government employee, as defined in section 202 of title 18, United States Code, who is not on an advisory committee or a chair or vice chair on an advisory committee may have direct or indirect communications in their official capacity with an agency or office that contracts with, regulates, or has a pending enforcement action against a large company\u2014\n**(1)**\nthat the special Government employee owns; or\n**(2)**\nfor which the special Government employee serves as a senior executive or director.\n##### (c) Regulations\nThe Office of Government Ethics shall promulgate regulations carrying out this section, including to define ownership of a large company.\n#### 5. Database of special Government employees\nSection 1103 of title 5, United States Code, is amended by adding at the end the following:\n(d) (1) In this subsection, the term covered individual \u2014 (A) means an individual who is a special Government employee who is not serving on an advisory committee; and (B) does not include an individual described in paragraph (1) or (2) of section 13107(a). (2) The Director, in coordination with the Office of Government Ethics, shall maintain to the extent technically practicable, keep current, and make available to the public over the internet, without a fee or other access charge, in a searchable, sortable, and downloadable manner, an electronic database that contains the name of each covered individual, a rolling tally of the number of days the person has served as a special Government employee, and a description of why the individual was designated as a special Government employee rather than a regular employee. .\n#### 6. Financial disclosure requirements of special Government employees\nTitle 5, United States Code, is amended\u2014\n**(1)**\nin section 13103(f)\u2014\n**(A)**\nin paragraph (8), by striking (other than a special Government employee) ;\n**(B)**\nin paragraph (11), by striking and at the end ;\n**(C)**\nin paragraph (12), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(13) A special Government employee who\u2014 (A) is not serving on an advisory committee or is serving as a chair or vice chair on an advisory committee; and (B) is not serving in a position classified as a general schedule position at the GS\u20139 level or below, with limited responsibilities, closely supervised by a career Federal employee. (14) For any special Government employee claiming an exemption from filing a public report this subsection, the relevant agency ethics officer shall review to ensure the exemption may be properly applied to that special Government employee. ; and\n**(2)**\nin section 13109(a)(1), by inserting , except as provided in section 13103(f)(13), after title 18) .\n#### 7. Modifications of online access to certain financial disclosure statements and related forms\nSection 1(a)(2) of the Act entitled An Act to modify the requirements under the STOCK Act regarding online access to certain financial disclosure statements and related forms , approved April 15, 2013 ( 5 U.S.C. 13107 note) is amended by adding at the end the following:\n(F) Any special Government employee of the executive branch who\u2014 (i) is not serving on an advisory committee or is serving as a chair or vice chair on an advisory committee; or (ii) is not serving in a position classified as a general schedule position at the GS\u20139 level or below, with limited responsibilities, closely supervised by a career Federal employee. .\n#### 8. Special Government employee rule\n##### (a) In general\nExcept as provided in subsection (b), in the case of a special Government employee, as defined in section 202 of title 18, United States Code, who has served in their department or agency for more than 60 days during the immediately preceding period of 365 consecutive days, all Federal ethics rules shall apply to such special Government employee to the same extent that such rules apply to regular Government employees.\n##### (b) Exception\nIn the case of a special Government employee, as defined in section 202 of title 18, United States Code, who has served in their department or agency for more than 130 during the immediately preceding period of 365 consecutive days, section 209 of title 18, United States Code, and subchapter III of chapter 131 of title 5, United States Code, shall apply to such special Government employee to the same extent that the section applies to regular Government employees, except that such section 209 shall apply whether the special Government employee serves with or without pay.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1491",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SEER Act 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-27T15:50:13Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2894ih.xml"
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
      "title": "SEER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SGE Ethics Enforcement Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to modify the definition of special Government employee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T05:34:10Z"
    }
  ]
}
```
