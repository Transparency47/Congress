# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5359
- Title: No Bribes for Politicians Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5359
- Origin chamber: House
- Introduced date: 2025-09-15
- Update date: 2025-09-25T15:30:40Z
- Update date including text: 2025-09-25T15:30:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-15: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-15: Introduced in House

## Actions

- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Introduced in House
- 2025-09-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5359",
    "number": "5359",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "No Bribes for Politicians Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-25T15:30:40Z",
    "updateDateIncludingText": "2025-09-25T15:30:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-15",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T16:00:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5359ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5359\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 15, 2025 Mr. Harder of California introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to require biannual financial disclosure reports for Federal officials, to prohibit certain acts by the President, the Vice President, and their families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Bribes for Politicians Act of 2025 .\n#### 2. Prohibition on using gifts in conjunction with Presidential duties\nSection 7342(c) of title 5, United States Code, is amended by inserting at the end the following:\n(4) If an employee deposits a tangible gift of more than minimal value with an agency and such gift is for official use in conjunction with Presidential duties\u2014 (A) such gift may not be used; and (C) the agency shall promptly dispose of such gift in accordance with subsection (e). .\n#### 3. Biannual financial disclosure requirement\nSection 13103(d) of title 5, United States Code, is amended to read as follows:\n(d) Biannual reports (1) In general Any individual who is an officer or employee described in subsection (f)\u2014 (A) during the 6-month period from January 1 to June 30 of any calendar year beginning with calendar year 2026 and performs the duties of the position or office for a period in excess of 60 days in such period shall file a report on or before October 15 of such calender year containing the information described in section 13104(a) of this title; and (B) during the 6-month period from July 1 to December 30 of any calendar year beginning with calendar year 2026 and performs the duties of the position or office for a period in excess of 60 days in such period shall file a report on or before May 15 of the succeeding calendar year containing the information described in such section 13104(a). (2) Application With respect to any report under paragraph (1), such section 13104(a) shall be applied by substituting applicable 6-month period for preceding calendar year .\n#### 4. Expansion of financial disclosure requirements to relatives of President, Vice President, and cabinet secretaries\n##### (a) In general\nSection 13104(e) of title 5, United States Code, is amended by inserting at the end the following new paragraph:\n(3) Reporting information relating to certain relatives (A) In general Consistent with subparagraph (B), each report required by subsection (d) of section 13103 of this title shall include the information listed in paragraphs (1) through (5) of subsection (a) of this section with respect to any relative of the reporting individual. (B) Application The requirements of subparagraph (A) shall only apply to the President, the Vice President, and any member of the President\u2019s cabinet. (C) Definition of relative In this paragraph, the term relative means an individual who is related to the reporting individual as father, mother, son, daughter, brother, sister, uncle, aunt, first cousin, nephew, niece, husband, wife, father-in-law, mother-in-law, son-in-law, daughter-in-law, brother-in-law, sister-in-law, stepfather, stepmother, stepson, stepdaughter, stepbrother, stepsister, half brother, or half sister. .\n##### (b) Technical and conforming amendments\nSection 13104(e) of title 5, United States Code, as amended by subsection (a), is further amended\u2014\n**(1)**\nin the subsection heading, by striking spouse or dependent child and inserting relatives ; and\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the paragraph heading, by striking I n general and inserting Reporting information relating to spouse or dependent child ; and\n**(B)**\nby striking each report required by section 13103 inserting each report required by subsections (a), (b), (c), and (e) of section 13103 .\n#### 5. Prohibitions on Presidential business activity\n##### (a) Prohibition\n**(1) In general**\nSubchapter III of chapter 131 of title 5, United States Code, is amended by inserting at the end the following:\n13147. Prohibitions on business activities of President and Vice President (a) Ownership prohibition The President and Vice President\u2014 (1) may not hold a financial interest in any firm, partnership, association, corporation, or other for-profit entity; and (2) shall divest, not later than 30 days after assuming office, of any such interest by converting any such interest into cash. (b) Name and likeness prohibition The President or Vice President, and the spouse or any dependent child of the President or Vice president, may not\u2014 (1) use the President\u2019s or Vice President\u2019s name or likeness for profit; or (2) permit the use of the President\u2019s or Vice President\u2019s name or likeness by any firm, partnership, association, corporation, or other for-profit entity. (c) Decision-Making prohibition The President and Vice President may not serve as an officer, board member, or in any other role which holds decision-making power at any firm, partnership, association, corporation, or other for-profit entity. (d) Exclusion This section shall not apply to any financial interest held in a retirement account, including any Federal, State, or local government employee retirement plan. .\n**(2) Clerical amendment**\nThe table of sections of such chapter is amended by inserting after the item relating to section 13146 the following:\n13147. Prohibitions on business activities of President and Vice President. .\n##### (b) Civil penalties\nSection 13145 of title 5, United States Code, is amended by striking section 13143 or 13144 and inserting section 13143, 13144, or 13147 .",
      "versionDate": "2025-09-15",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-25T15:30:40Z"
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
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5359ih.xml"
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
      "title": "No Bribes for Politicians Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Bribes for Politicians Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to require biannual financial disclosure reports for Federal officials, to prohibit certain acts by the President, the Vice President, and their families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:30Z"
    }
  ]
}
```
