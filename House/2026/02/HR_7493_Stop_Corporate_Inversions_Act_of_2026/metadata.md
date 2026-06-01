# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7493
- Title: Stop Corporate Inversions Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7493
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-02-27T21:39:20Z
- Update date including text: 2026-02-27T21:39:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7493",
    "number": "7493",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Stop Corporate Inversions Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-27T21:39:20Z",
    "updateDateIncludingText": "2026-02-27T21:39:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7493ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7493\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Doggett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the rules relating to inverted corporations.\n#### 1. Short title\nThis Act may be cited as the Stop Corporate Inversions Act of 2026 .\n#### 2. Modifications to rules relating to inverted corporations\n##### (a) In general\nSubsection (b) of section 7874 of the Internal Revenue Code of 1986 is amended to read as follows:\n(b) Inverted corporations treated as domestic corporations (1) In general Notwithstanding section 7701(a)(4), a foreign corporation shall be treated for purposes of this title as a domestic corporation if\u2014 (A) such corporation would be a surrogate foreign corporation if subsection (a)(2) were applied by substituting 80 percent for 60 percent , or (B) such corporation is an inverted domestic corporation. (2) Inverted domestic corporation For purposes of this subsection, a foreign corporation shall be treated as an inverted domestic corporation if, pursuant to a plan (or a series of related transactions)\u2014 (A) the entity completes after May 8, 2014, the direct or indirect acquisition of\u2014 (i) substantially all of the properties held directly or indirectly by a domestic corporation, or (ii) substantially all of the assets of, or substantially all of the properties constituting a trade or business of, a domestic partnership, and (B) after the acquisition, either\u2014 (i) more than 50 percent of the stock (by vote or value) of the entity is held\u2014 (I) in the case of an acquisition with respect to a domestic corporation, by former shareholders of the domestic corporation by reason of holding stock in the domestic corporation, or (II) in the case of an acquisition with respect to a domestic partnership, by former partners of the domestic partnership by reason of holding a capital or profits interest in the domestic partnership, or (ii) the management and control of the expanded affiliated group which includes the entity occurs, directly or indirectly, primarily within the United States, and such expanded affiliated group has significant domestic business activities. (3) Exception for corporations with substantial business activities in foreign country of organization A foreign corporation described in paragraph (2) shall not be treated as an inverted domestic corporation if after the acquisition the expanded affiliated group which includes the entity has substantial business activities in the foreign country in which or under the law of which the entity is created or organized when compared to the total business activities of such expanded affiliated group. For purposes of subsection (a)(2)(B)(iii) and the preceding sentence, the term substantial business activities shall have the meaning given such term under regulations in effect on January 18, 2017, except that the Secretary may issue regulations increasing the threshold percent in any of the tests under such regulations for determining if business activities constitute substantial business activities for purposes of this paragraph. (4) Management and control For purposes of paragraph (2)(B)(ii)\u2014 (A) In general The Secretary shall prescribe regulations for purposes of determining cases in which the management and control of an expanded affiliated group is to be treated as occurring, directly or indirectly, primarily within the United States. The regulations prescribed under the preceding sentence shall apply to periods after May 8, 2014. (B) Executive officers and senior management Such regulations shall provide that the management and control of an expanded affiliated group shall be treated as occurring, directly or indirectly, primarily within the United States if substantially all of the executive officers and senior management of the expanded affiliated group who exercise day-to-day responsibility for making decisions involving strategic, financial, and operational policies of the expanded affiliated group are based or primarily located within the United States. Individuals who in fact exercise such day-to-day responsibilities shall be treated as executive officers and senior management regardless of their title. (5) Significant domestic business activities For purposes of paragraph (2)(B)(ii), an expanded affiliated group has significant domestic business activities if at least 25 percent of\u2014 (A) the employees of the group are based in the United States, (B) the employee compensation incurred by the group is incurred with respect to employees based in the United States, (C) the assets of the group are located in the United States, or (D) the income of the group is derived in the United States, determined in the same manner as such determinations are made for purposes of determining substantial business activities under regulations referred to in paragraph (3) as in effect on January 18, 2017, but applied by treating all references in such regulations to foreign country and relevant foreign country as references to the United States . The Secretary may issue regulations decreasing the threshold percent in any of the tests under such regulations for determining if business activities constitute significant domestic business activities for purposes of this paragraph. .\n##### (b) Conforming amendments\n**(1)**\nClause (i) of section 7874(a)(2)(B) of such Code is amended by striking after March 4, 2003, and inserting after March 4, 2003, and before May 8, 2014, .\n**(2)**\nSubsection (c) of section 7874 of such Code is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking subsection (a)(2)(B)(ii) and inserting subsections (a)(2)(B)(ii) and (b)(2)(B)(i) ; and\n**(ii)**\nby inserting or (b)(2)(A) after (a)(2)(B)(i) in subparagraph (B);\n**(B)**\nin paragraph (3), by inserting or (b)(2)(B)(i), as the case may be, after (a)(2)(B)(ii) ;\n**(C)**\nin paragraph (5), by striking subsection (a)(2)(B)(ii) and inserting subsections (a)(2)(B)(ii) and (b)(2)(B)(i) ; and\n**(D)**\nin paragraph (6), by inserting or inverted domestic corporation, as the case may be, after surrogate foreign corporation .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after May 8, 2014.",
      "versionDate": "2026-02-11",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "995",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax Breaks for Outsourcing Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-05",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "409",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax Breaks for Outsourcing Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-11",
        "text": "Read twice and referred to the Committee on Finance. (text: CR S579-580)"
      },
      "number": "3847",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Corporate Inversions Act of 2026",
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
        "name": "Taxation",
        "updateDate": "2026-02-20T20:29:01Z"
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
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7493ih.xml"
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
      "title": "Stop Corporate Inversions Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Corporate Inversions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the rules relating to inverted corporations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:39Z"
    }
  ]
}
```
