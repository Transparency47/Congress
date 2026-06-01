# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1515?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1515
- Title: GOOD Act
- Congress: 119
- Bill type: HR
- Bill number: 1515
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-03-28T08:06:18Z
- Update date including text: 2026-03-28T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 15:41:17 - Floor: Mr. Comer moved to suspend the rules and pass the bill.
- 2025-03-03 15:41:28 - Floor: Considered under suspension of the rules. (consideration: CR H928-930)
- 2025-03-03 15:41:30 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1515.
- 2025-03-03 15:50:56 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)
- 2025-03-03 15:50:56 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)
- 2025-03-03 15:50:59 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-03-04 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-03-03 15:41:17 - Floor: Mr. Comer moved to suspend the rules and pass the bill.
- 2025-03-03 15:41:28 - Floor: Considered under suspension of the rules. (consideration: CR H928-930)
- 2025-03-03 15:41:30 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 1515.
- 2025-03-03 15:50:56 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)
- 2025-03-03 15:50:56 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)
- 2025-03-03 15:50:59 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-03-04 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1515",
    "number": "1515",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001108",
        "district": "1",
        "firstName": "James",
        "fullName": "Rep. Comer, James [R-KY-1]",
        "lastName": "Comer",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "GOOD Act",
    "type": "HR",
    "updateDate": "2026-03-28T08:06:18Z",
    "updateDateIncludingText": "2026-03-28T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-03-03",
      "actionTime": "15:50:59",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-03-03",
      "actionTime": "15:50:56",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-03-03",
      "actionTime": "15:50:56",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H928-929)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-03-03",
      "actionTime": "15:41:30",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 1515.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-03-03",
      "actionTime": "15:41:28",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H928-930)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-03-03",
      "actionTime": "15:41:17",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Comer moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-03-04T17:41:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-24T17:03:50Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1515\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Comer (for himself and Mr. Khanna ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo increase access to agency guidance documents.\n#### 1. Short title\nThis Act may be cited as the Guidance Out Of Darkness Act or the GOOD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Guidance document**\n**(A) In general**\nThe term guidance document \u2014\n**(i)**\nmeans an agency statement of general applicability (other than a rule that has the force and effect of law promulgated in accordance with the notice and comment procedures under section 553 of title 5, United States Code) that\u2014\n**(I)**\ndoes not have the force and effect of law; and\n**(II)**\nis designated by an agency official as setting forth\u2014\n**(aa)**\na policy on a statutory, regulatory, or technical issue; or\n**(bb)**\nan interpretation of a statutory or regulatory issue; and\n**(ii)**\nmay include\u2014\n**(I)**\na memorandum;\n**(II)**\na notice;\n**(III)**\na bulletin;\n**(IV)**\na directive;\n**(V)**\na news release;\n**(VI)**\na letter;\n**(VII)**\na blog post;\n**(VIII)**\na no-action letter;\n**(IX)**\na speech by an agency official; and\n**(X)**\nany combination of the items described in subclauses (I) through (IX).\n**(B) Rule of construction**\nThe term guidance document \u2014\n**(i)**\nshall be construed broadly to effectuate the purpose and intent of this Act; and\n**(ii)**\nshall not be limited to the items described in subparagraph (A)(ii).\n#### 3. Publication of guidance documents on the internet\n##### (a) In general\nSubject to section 5, on the date on which an agency issues a guidance document, the agency shall publish the guidance document in accordance with the requirements under section 4.\n##### (b) Previously issued guidance documents\nSubject to section 5, not later than 180 days after the date of enactment of this Act, each agency shall publish, in accordance with the requirements under section 4, any guidance document issued by that agency that is in effect on that date.\n#### 4. Single location\n##### (a) In general\nAll guidance documents published under section 3 by an agency shall be published in a single location on an internet website designated by the Director under subsection (d).\n##### (b) Agency internet websites\nEach agency shall, for guidance documents published by the agency under section 3, publish a hyperlink on the internet website of the agency that provides access to the guidance documents at the location described in subsection (a).\n##### (c) Organization\n**(1) In general**\nThe guidance documents described in subsection (a) shall be\u2014\n**(A)**\ncategorized as guidance documents; and\n**(B)**\nfurther divided into subcategories as appropriate.\n**(2) Agency internet websites**\nThe hyperlinks described in subsection (b) shall be prominently displayed on the internet website of the agency.\n##### (d) Designation\nNot later than 90 days after the date of enactment of this Act, the Director shall designate an internet website on which guidance documents shall be published under section 3.\n#### 5. Documents and information exempt from disclosure under FOIA\nIf a guidance document issued by an agency is a document that is exempt from disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ), or contains information that is exempt from disclosure under that section, that document or information, as the case may be, shall not be subject to the requirements under this Act.\n#### 6. Rescinded guidance documents\nOn the date on which a guidance document issued by an agency is rescinded, or, in the case of a guidance document that is rescinded pursuant to a court order, not later than the date on which the order is entered, the agency shall, at the location described in section 4(a)\u2014\n**(1)**\nmaintain the rescinded guidance document; and\n**(2)**\nindicate\u2014\n**(A)**\nthat the guidance document is rescinded;\n**(B)**\nif the guidance document was rescinded pursuant to a court order, the case number of the case in which the order was entered; and\n**(C)**\nthe date on which the guidance document was rescinded.\n#### 7. Rules of construction\n##### (a) Validity of guidance documents\nNothing in this Act shall be construed to mean that noncompliance with any provision of this Act affects or otherwise impacts the validity of any guidance document.\n##### (b) Congressional review of guidance documents\nNothing in this Act shall be construed to affect or otherwise impact whether a guidance document is subject to congressional review under chapter 8 of title 5, United States Code.\n#### 8. Report on agency compliance\nNot later than 5 years after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on agency compliance with this Act.",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 1515\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Received; read twice and referred to the Committee on Homeland Security and Governmental Affairs\nAN ACT\nTo increase access to agency guidance documents.\n#### 1. Short title\nThis Act may be cited as the Guidance Out Of Darkness Act or the GOOD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Guidance document**\n**(A) In general**\nThe term guidance document \u2014\n**(i)**\nmeans an agency statement of general applicability (other than a rule that has the force and effect of law promulgated in accordance with the notice and comment procedures under section 553 of title 5, United States Code) that\u2014\n**(I)**\ndoes not have the force and effect of law; and\n**(II)**\nis designated by an agency official as setting forth\u2014\n**(aa)**\na policy on a statutory, regulatory, or technical issue; or\n**(bb)**\nan interpretation of a statutory or regulatory issue; and\n**(ii)**\nmay include\u2014\n**(I)**\na memorandum;\n**(II)**\na notice;\n**(III)**\na bulletin;\n**(IV)**\na directive;\n**(V)**\na news release;\n**(VI)**\na letter;\n**(VII)**\na blog post;\n**(VIII)**\na no-action letter;\n**(IX)**\na speech by an agency official; and\n**(X)**\nany combination of the items described in subclauses (I) through (IX).\n**(B) Rule of construction**\nThe term guidance document \u2014\n**(i)**\nshall be construed broadly to effectuate the purpose and intent of this Act; and\n**(ii)**\nshall not be limited to the items described in subparagraph (A)(ii).\n#### 3. Publication of guidance documents on the internet\n##### (a) In general\nSubject to section 5, on the date on which an agency issues a guidance document, the agency shall publish the guidance document in accordance with the requirements under section 4.\n##### (b) Previously issued guidance documents\nSubject to section 5, not later than 180 days after the date of enactment of this Act, each agency shall publish, in accordance with the requirements under section 4, any guidance document issued by that agency that is in effect on that date.\n#### 4. Single location\n##### (a) In general\nAll guidance documents published under section 3 by an agency shall be published in a single location on an internet website designated by the Director under subsection (d).\n##### (b) Agency internet websites\nEach agency shall, for guidance documents published by the agency under section 3, publish a hyperlink on the internet website of the agency that provides access to the guidance documents at the location described in subsection (a).\n##### (c) Organization\n**(1) In general**\nThe guidance documents described in subsection (a) shall be\u2014\n**(A)**\ncategorized as guidance documents; and\n**(B)**\nfurther divided into subcategories as appropriate.\n**(2) Agency internet websites**\nThe hyperlinks described in subsection (b) shall be prominently displayed on the internet website of the agency.\n##### (d) Designation\nNot later than 90 days after the date of enactment of this Act, the Director shall designate an internet website on which guidance documents shall be published under section 3.\n#### 5. Documents and information exempt from disclosure under FOIA\nIf a guidance document issued by an agency is a document that is exempt from disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ), or contains information that is exempt from disclosure under that section, that document or information, as the case may be, shall not be subject to the requirements under this Act.\n#### 6. Rescinded guidance documents\nOn the date on which a guidance document issued by an agency is rescinded, or, in the case of a guidance document that is rescinded pursuant to a court order, not later than the date on which the order is entered, the agency shall, at the location described in section 4(a)\u2014\n**(1)**\nmaintain the rescinded guidance document; and\n**(2)**\nindicate\u2014\n**(A)**\nthat the guidance document is rescinded;\n**(B)**\nif the guidance document was rescinded pursuant to a court order, the case number of the case in which the order was entered; and\n**(C)**\nthe date on which the guidance document was rescinded.\n#### 7. Rules of construction\n##### (a) Validity of guidance documents\nNothing in this Act shall be construed to mean that noncompliance with any provision of this Act affects or otherwise impacts the validity of any guidance document.\n##### (b) Congressional review of guidance documents\nNothing in this Act shall be construed to affect or otherwise impact whether a guidance document is subject to congressional review under chapter 8 of title 5, United States Code.\n#### 8. Report on agency compliance\nNot later than 5 years after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on agency compliance with this Act.",
      "versionDate": "2025-03-04",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1515\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo increase access to agency guidance documents.\n#### 1. Short title\nThis Act may be cited as the Guidance Out Of Darkness Act or the GOOD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given the term in section 551 of title 5, United States Code.\n**(2) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(3) Guidance document**\n**(A) In general**\nThe term guidance document \u2014\n**(i)**\nmeans an agency statement of general applicability (other than a rule that has the force and effect of law promulgated in accordance with the notice and comment procedures under section 553 of title 5, United States Code) that\u2014\n**(I)**\ndoes not have the force and effect of law; and\n**(II)**\nis designated by an agency official as setting forth\u2014\n**(aa)**\na policy on a statutory, regulatory, or technical issue; or\n**(bb)**\nan interpretation of a statutory or regulatory issue; and\n**(ii)**\nmay include\u2014\n**(I)**\na memorandum;\n**(II)**\na notice;\n**(III)**\na bulletin;\n**(IV)**\na directive;\n**(V)**\na news release;\n**(VI)**\na letter;\n**(VII)**\na blog post;\n**(VIII)**\na no-action letter;\n**(IX)**\na speech by an agency official; and\n**(X)**\nany combination of the items described in subclauses (I) through (IX).\n**(B) Rule of construction**\nThe term guidance document \u2014\n**(i)**\nshall be construed broadly to effectuate the purpose and intent of this Act; and\n**(ii)**\nshall not be limited to the items described in subparagraph (A)(ii).\n#### 3. Publication of guidance documents on the internet\n##### (a) In general\nSubject to section 5, on the date on which an agency issues a guidance document, the agency shall publish the guidance document in accordance with the requirements under section 4.\n##### (b) Previously issued guidance documents\nSubject to section 5, not later than 180 days after the date of enactment of this Act, each agency shall publish, in accordance with the requirements under section 4, any guidance document issued by that agency that is in effect on that date.\n#### 4. Single location\n##### (a) In general\nAll guidance documents published under section 3 by an agency shall be published in a single location on an internet website designated by the Director under subsection (d).\n##### (b) Agency internet websites\nEach agency shall, for guidance documents published by the agency under section 3, publish a hyperlink on the internet website of the agency that provides access to the guidance documents at the location described in subsection (a).\n##### (c) Organization\n**(1) In general**\nThe guidance documents described in subsection (a) shall be\u2014\n**(A)**\ncategorized as guidance documents; and\n**(B)**\nfurther divided into subcategories as appropriate.\n**(2) Agency internet websites**\nThe hyperlinks described in subsection (b) shall be prominently displayed on the internet website of the agency.\n##### (d) Designation\nNot later than 90 days after the date of enactment of this Act, the Director shall designate an internet website on which guidance documents shall be published under section 3.\n#### 5. Documents and information exempt from disclosure under FOIA\nIf a guidance document issued by an agency is a document that is exempt from disclosure under section 552(b) of title 5, United States Code (commonly known as the Freedom of Information Act ), or contains information that is exempt from disclosure under that section, that document or information, as the case may be, shall not be subject to the requirements under this Act.\n#### 6. Rescinded guidance documents\nOn the date on which a guidance document issued by an agency is rescinded, or, in the case of a guidance document that is rescinded pursuant to a court order, not later than the date on which the order is entered, the agency shall, at the location described in section 4(a)\u2014\n**(1)**\nmaintain the rescinded guidance document; and\n**(2)**\nindicate\u2014\n**(A)**\nthat the guidance document is rescinded;\n**(B)**\nif the guidance document was rescinded pursuant to a court order, the case number of the case in which the order was entered; and\n**(C)**\nthe date on which the guidance document was rescinded.\n#### 7. Rules of construction\n##### (a) Validity of guidance documents\nNothing in this Act shall be construed to mean that noncompliance with any provision of this Act affects or otherwise impacts the validity of any guidance document.\n##### (b) Congressional review of guidance documents\nNothing in this Act shall be construed to affect or otherwise impact whether a guidance document is subject to congressional review under chapter 8 of title 5, United States Code.\n#### 8. Report on agency compliance\nNot later than 5 years after the date of enactment of this Act, the Comptroller General shall submit to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on agency compliance with this Act.",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
            "updateDate": "2025-03-05T16:06:54Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-05T16:06:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-03-04T20:21:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
    "originChamber": "House",
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
          "measure-id": "id119hr1515",
          "measure-number": "1515",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1515v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Guidance Out Of Darkness Act or the GOOD Act</strong></p><p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p><p>The documents must be categorized as guidance documents and further divided into subcategories.</p><p>No later than five years after the enactment of this bill, the Government Accountability Office must report on agency compliance with these requirements.</p>"
        },
        "title": "GOOD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1515.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guidance Out Of Darkness Act or the GOOD Act</strong></p><p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p><p>The documents must be categorized as guidance documents and further divided into subcategories.</p><p>No later than five years after the enactment of this bill, the Government Accountability Office must report on agency compliance with these requirements.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr1515"
    },
    "title": "GOOD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guidance Out Of Darkness Act or the GOOD Act</strong></p><p>This bill establishes requirements concerning the posting of agency guidance documents. Specifically, an agency must publish guidance documents online on the dates they are issued, publish all of its guidance documents that are in effect in a single location on a designated website, display a hyperlink on its website that provides access to the guidance documents on such website, and indicate on such website if a guidance document has been rescinded.</p><p>The documents must be categorized as guidance documents and further divided into subcategories.</p><p>No later than five years after the enactment of this bill, the Government Accountability Office must report on agency compliance with these requirements.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119hr1515"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1515eh.xml"
        }
      ],
      "type": "Engrossed in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "GOOD Act",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-03-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "RFS",
      "billTextVersionName": "Referred in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Guidance Out Of Darkness Act",
      "titleType": "Short Titles from RFS (Referred to Senate) bill text",
      "titleTypeCode": "255",
      "updateDate": "2025-03-07T04:23:18Z"
    },
    {
      "title": "GOOD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:21Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "GOOD Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Guidance Out Of Darkness Act",
      "titleType": "Short Title(s) as Passed House",
      "titleTypeCode": "104",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guidance Out Of Darkness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GOOD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase access to agency guidance documents.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:30Z"
    }
  ]
}
```
