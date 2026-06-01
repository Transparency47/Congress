# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8111
- Title: Bankruptcy Venue Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 8111
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-14T19:18:59Z
- Update date including text: 2026-04-14T19:18:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8111",
    "number": "8111",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000397",
        "district": "18",
        "firstName": "Zoe",
        "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
        "lastName": "Lofgren",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Bankruptcy Venue Reform Act",
    "type": "HR",
    "updateDate": "2026-04-14T19:18:59Z",
    "updateDateIncludingText": "2026-04-14T19:18:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8111ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8111\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Lofgren (for herself and Mr. Cline ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to modify venue requirements relating to bankruptcy proceedings.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Venue Reform Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds that\u2014\n**(1)**\nbankruptcy law provides a number of venue options for filing bankruptcy under chapter 11 of title 11, United States Code, including, with respect to the entity filing bankruptcy\u2014\n**(A)**\nany district in which the place of incorporation of the entity is located;\n**(B)**\nany district in which the principal place of business or principal assets of the entity are located; and\n**(C)**\nany district in which an affiliate of the entity has filed a pending case under title 11, United States Code;\n**(2)**\nthe wide range of permissible bankruptcy venue options has led to an increase in companies filing for bankruptcy outside of their home States\u2014the district in which the principal place of business or principal assets of the company is located;\n**(3)**\nthe practice described in paragraph (2) is known as forum shopping ;\n**(4)**\nforum shopping has resulted in a concentration of bankruptcy cases in a limited number of districts;\n**(5)**\nforum shopping\u2014\n**(A)**\nprevents small businesses, employees, retirees, creditors, and other important stakeholders from fully participating in bankruptcy cases that have tremendous impacts on their lives, communities, and local economies; and\n**(B)**\ndeprives district courts of the United States of the opportunity to contribute to the development of bankruptcy law in the jurisdictions of those district courts; and\n**(6)**\nreducing forum shopping in the bankruptcy system will strengthen the integrity of, and build public confidence and ensure fairness in, the bankruptcy system.\n##### (b) Purpose\nThe purpose of this Act is to prevent the practice of forum shopping in cases filed under chapter 11 of title 11, United States Code.\n#### 3. Venue of cases under title 11\nTitle 28, United States Code, is amended\u2014\n**(1)**\nby striking section 1408 and inserting the following:\n1408. Venue of cases under title 11 (a) Principal place of business with respect to certain entities (1) In general Except as provided in paragraph (2), for the purposes of this section, if an entity is subject to the reporting requirements of section 13 or 15(d) of the Securities Exchange clause 1934 ( 15 U.S.C. 78m , 78o(d)), the term principal place of business , with respect to the entity, means the address of the principal executive office of the entity as stated in the last annual report filed under that Act before the commencement of a case under title 11 of which the entity is the subject. (2) Exception With respect to an entity described in paragraph (1), the definition of the principal place of business under that paragraph shall apply for purposes of this section unless another address is shown to be the principal place of business of the entity by clear and convincing evidence. (b) Venue Except as provided in section 1410, a case under title 11 may be commenced only in the district court for the district\u2014 (1) in which the domicile, residence, or principal assets in the United States of an individual who is the subject of the case have been located\u2014 (A) for the 180 days immediately preceding such commencement; or (B) for a longer portion of the 180-day period immediately preceding such commencement than the domicile, residence, or principal assets in the United States of the individual were located in any other district; (2) in which the principal place of business or principal assets in the United States of an entity, other than an individual, that is the subject of the case have been located\u2014 (A) for the 180 days immediately preceding such commencement; or (B) for a longer portion of the 180-day period immediately preceding such commencement than the principal place of business or principal assets in the United States of the entity were located in any other district; or (3) in which there is pending a case under title 11 concerning an affiliate that directly or indirectly owns, controls, or holds 50 percent or more of the outstanding voting securities of, or is the general partner of, the entity that is the subject of the later filed case, but only if the pending case was properly filed in that district in accordance with this section. (c) Limitations (1) In general For the purposes of paragraphs (2) and (3) of subsection (b), no effect shall be given to a change in the ownership or control of an entity that is the subject of the case, or of an affiliate of the entity, or to a transfer of the principal place of business or principal assets in the United States of an entity that is the subject of the case, or of an affiliate of the entity, to another district, that takes place\u2014 (A) within 1 year before the date on which the case is commenced; or (B) for the purpose of establishing venue. (2) Principal assets (A) Principal assets of an entity other than an individual For the purposes of subsection (b)(2) and paragraph (1) of this subsection\u2014 (i) the term principal assets does not include cash or cash equivalents; and (ii) any equity interest in an affiliate is located in the district in which the holder of the equity interest has its principal place of business in the United States, as determined in accordance with subsection (b)(2). (B) Equity interests of individuals For the purposes of subsection (b)(1), if the holder of any equity interest in an affiliate is an individual, the equity interest is located in the district in which the domicile or residence in the United States of the holder of the equity interest is located, as determined in accordance with subsection (b)(1). (d) Burden On any objection to, or request to change, venue under paragraph (2) or (3) of subsection (b) of a case under title 11, the entity that commences the case shall bear the burden of establishing by clear and convincing evidence that venue is proper under this section. (e) Out-of-State admission for government attorneys The Supreme Court shall prescribe rules, in accordance with section 2075, for cases or proceedings arising under title 11, or arising in or related to cases under title 11, to allow any attorney representing a governmental unit to be permitted to appear on behalf of the governmental unit and intervene without charge, and without meeting any requirement under any local court rule relating to attorney appearances or the use of local counsel, before any bankruptcy court, district court, or bankruptcy appellate panel. ; and\n**(2)**\nby striking section 1412 and inserting the following:\n1412. Change of venue (a) In general Notwithstanding that a case or proceeding under title 11, or arising in or related to a case under title 11, is filed in the correct division or district, a district court may transfer the case or proceeding to a district court for another district or division\u2014 (1) in the interest of justice; or (2) for the convenience of the parties. (b) Incorrectly filed cases or proceedings If a case or proceeding under title 11, or arising in or related to a case under title 11, is filed in a division or district that is improper under section 1408(b), the district court shall\u2014 (1) immediately dismiss the case or proceeding; or (2) if it is in the interest of justice, immediately transfer the case or proceeding to any district court for any district or division in which the case or proceeding could have been brought. (c) Objections and requests relating to changes in venue Not later than 14 days after the filing of an objection to, or a request to change, venue of a case or proceeding under title 11, or arising in or related to a case under title 11, the court shall enter an order granting or denying the objection or request. .",
      "versionDate": "2026-03-26",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-14T19:18:59Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8111ih.xml"
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
      "title": "Bankruptcy Venue Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bankruptcy Venue Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to modify venue requirements relating to bankruptcy proceedings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:22Z"
    }
  ]
}
```
