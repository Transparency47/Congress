# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4009
- Title: Pro Codes Act
- Congress: 119
- Bill type: HR
- Bill number: 4009
- Origin chamber: House
- Introduced date: 2025-06-13
- Update date: 2026-04-01T14:04:59Z
- Update date including text: 2026-04-01T14:04:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-13: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-13: Introduced in House

## Actions

- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Introduced in House
- 2025-06-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-13",
    "latestAction": {
      "actionDate": "2025-06-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4009",
    "number": "4009",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Pro Codes Act",
    "type": "HR",
    "updateDate": "2026-04-01T14:04:59Z",
    "updateDateIncludingText": "2026-04-01T14:04:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-13",
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
      "actionDate": "2025-06-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-13",
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
          "date": "2025-06-13T13:30:40Z",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4009ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4009\nIN THE HOUSE OF REPRESENTATIVES\nJune 13, 2025 Mr. Issa (for himself and Ms. Ross ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 17, United States Code, to reaffirm the importance of, and include requirements for, works incorporated by reference into law, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting and Enhancing Public Access to Codes Act or the Pro Codes Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress, the executive branch, and State and local governments have long recognized that the people of the United States benefit greatly from the work of private standards development organizations with expertise in highly specialized areas.\n**(2)**\nThe organizations described in paragraph (1) create technical standards and voluntary consensus standards through a process requiring openness, balance, consensus, and due process to ensure all interested parties have an opportunity to participate in standards development.\n**(3)**\nThe standards that result from the process described in paragraph (2) are used by private industry, academia, the Federal Government, and State and local governments that incorporate those standards by reference into laws and regulations.\n**(4)**\nThe standards described in paragraph (3) further innovation, commerce, and public safety, all without cost to governments or taxpayers because standards development organizations fund the process described in paragraph (2) through the sale and licensing of their standards.\n**(5)**\nCongress and the executive branch have repeatedly declared that, wherever possible, governments should rely on voluntary consensus standards and have set forth policies and procedures by which those standards are incorporated by reference into laws and regulations and that balance the interests of access with protection for copyright.\n**(6)**\nCircular A\u2013119 of the Office of Management and Budget entitled Federal Participation in the Development and Use of Voluntary Consensus Standards and in Conformity Assessment Activities , issued in revised form on January 27, 2016, recognizes the benefits of voluntary consensus standards and incorporation by reference, stating that [i]f a standard is used and published in an agency document, your agency must observe and protect the rights of the copyright holder and meet any other similar obligations. .\n**(7)**\nFederal agencies have relied extensively on the incorporation by reference system to leverage the value of technical standards and voluntary consensus standards for the benefit of the public, resulting in more than 23,000 sections in the Code of Federal Regulations that incorporate by reference technical and voluntary consensus standards.\n**(8)**\nState and local governments have also recognized that technical standards and voluntary consensus standards are critical to protecting public health and safety, which has resulted in many such governments\u2014\n**(A)**\nincorporating those standards by reference into their laws and regulations; or\n**(B)**\nentering into license agreements with standards development organizations to use the standards created by those organizations.\n**(9)**\nStandards development organizations rely on copyright protection to generate the revenues necessary to fund the voluntary consensus process and to continue creating and updating these important standards.\n**(10)**\nThe people of the United States have a strong interest in\u2014\n**(A)**\nensuring that standards development organizations continue to utilize a voluntary consensus process\u2014\n**(i)**\nin which all interested parties can participate; and\n**(ii)**\nthat continues to create and update standards in a timely manner to\u2014\n**(I)**\naccount for technological advances;\n**(II)**\naddress new threats to public health and safety; and\n**(III)**\nimprove the usefulness of those standards; and\n**(B)**\nthe provision of access that allows people to read technical and voluntary consensus standards that are incorporated by reference into laws and regulations.\n**(11)**\nAs of the date of enactment of this Act, many standards development organizations make their standards available to the public free of charge online in a manner that does not substantially disrupt the ability of those organizations to earn revenue from the industries and professionals that purchase copies and subscription-access to those standards (such as through read-only access), which ensures that the public may read the current, accurate version of such a standard without significantly interfering with the revenue model that has long supported those organizations and their creation of, and investment in, new standards.\n**(12)**\nThrough this Act, and the amendments made by this Act, Congress intends to balance the goals of furthering the creation of standards and ensuring public access to standards that are incorporated by reference into law or regulation.\n#### 3. Works incorporated by reference into law\n##### (a) In general\nChapter 1 of title 17, United States Code, is amended by adding at the end the following:\n123. Works incorporated by reference into law (a) Definitions In this section: (1) Circular A\u2013119 The term Circular A\u2013119 means Circular A\u2013119 of the Office of Management and Budget entitled Federal Participation in the Development and Use of Voluntary Consensus Standards and in Conformity Assessment Activities , issued in revised form on January 27, 2016. (2) Incorporated by reference (A) In general The term incorporated by reference means, with respect to a standard, that the text of a Federal, State, local, or municipal law or regulation\u2014 (i) references all or part of the standard; and (ii) does not copy the text of that standard directly into that law or regulation. (B) Application The creation or publication of a work that includes both the text of a law or regulation and all or part of a standard that has been incorporated by reference, as described in subparagraph (A), shall not affect the status of the standard as incorporated by reference under that subparagraph. (3) Standard The term standard means a standard or code that is\u2014 (A) a technical standard, as that term is defined in section 12(d) of the National Technology Transfer and Advancement Act of 1995 ( 15 U.S.C. 272 note); or (B) a voluntary consensus standard, as that term is used for the purposes of Circular A\u2013119. (4) Standards development organization The term standards development organization means a holder of a copyright under this title that plans, develops, establishes, or coordinates voluntary consensus standards using procedures that incorporate the attributes of openness, balance of interests, due process, an appeals process, and consensus in a manner consistent with the requirements of Circular A\u2013119. (5) Publicly accessible online (A) In general The term publicly accessible online , with respect to material, means that the material is displayed for review in a readily accessible manner on a public website that conforms with the accessibility requirements of section 508 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794d ), including the regulations implementing that section as set forth in part 1194 of title 36, Code of Federal Regulations, or any successor regulation. (B) Rule of construction If a user is required to create an account or agree to the terms of service of a website or organization in order to access material online, that requirement shall not be construed to render the material not publicly accessible online for the purposes of subparagraph (A), if\u2014 (i) there is no monetary cost to the user to access that material; and (ii) no personally identifiable information collected pursuant to such a requirement is used without the affirmative and express consent of the user. (b) Standards incorporated by reference into law or regulation A standard to which copyright protection subsists under section 102(a) at the time of its fixation shall retain such protection, notwithstanding that the standard is incorporated by reference, if the applicable standards development organization, within a reasonable period of time after obtaining actual or constructive notice that the standard has been incorporated by reference, makes all portions of the standard so incorporated publicly accessible online at no monetary cost and in a format that includes a searchable table of contents and index, or equivalent aids to facilitate the location of specific content. (c) Burden of proof In any proceeding in which a party asserts that a standards development organization has failed to comply with the requirements under subsection (b) for retaining copyright protection with respect to a standard, the burden of proof shall be on the party making that assertion to prove that the standards development organization has failed to comply with those requirements. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 1 of title 17, United States Code, is amended by adding at the end the following:\n123. Works incorporated by reference into law. .\n#### 4. Study of standards cost to governments\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study on the financial impact to Federal, State, and local governments in the United States associated with acquiring access to standards incorporated by reference into law.\n##### (b) Scope\nThe study under subsection (a) shall\u2014\n**(1)**\nanalyze the total expenditure by government entities for accessing these standards;\n**(2)**\nassess any financial burdens or resource constraints these costs impose on governments, particularly for smaller municipalities;\n**(3)**\nevaluate the cost-effectiveness of current mechanisms for acquiring these standards; and\n**(4)**\nexamine the impacts on public services due to the costs associated with accessing these standards.\n##### (c) Report\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General shall submit a report to Congress that includes\u2014\n**(1)**\nthe findings of the study conducted under subsection (a); and\n**(2)**\nrecommendations to mitigate any adverse financial impacts identified by the study, including suggestions for legislative or administrative actions as appropriate.",
      "versionDate": "2025-06-13",
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
        "actionDate": "2026-03-19",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "4145",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pro Codes Act of 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4072",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pro Codes Act",
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
        "name": "Commerce",
        "updateDate": "2025-07-07T13:19:50Z"
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
      "date": "2025-06-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4009ih.xml"
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
      "title": "Pro Codes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pro Codes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting and Enhancing Public Access to Codes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 17, United States Code, to reaffirm the importance of, and include requirements for, works incorporated by reference into law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T04:48:29Z"
    }
  ]
}
```
