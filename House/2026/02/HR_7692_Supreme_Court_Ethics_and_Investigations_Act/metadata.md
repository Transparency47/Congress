# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7692?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7692
- Title: Supreme Court Ethics and Investigations Act
- Congress: 119
- Bill type: HR
- Bill number: 7692
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-28T08:06:19Z
- Update date including text: 2026-04-28T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7692",
    "number": "7692",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Supreme Court Ethics and Investigations Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:19Z",
    "updateDateIncludingText": "2026-04-28T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:03:45Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "TX"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7692ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7692\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Goldman of New York (for himself, Mr. Johnson of Georgia , Mr. Nadler , Ms. Norton , Mr. Tonko , Mr. Thanedar , Ms. Garcia of Texas , Mr. Krishnamoorthi , Mr. Ivey , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to establish an Office of Ethics Counsel and an Office of Investigative Counsel within the Supreme Court of the United States.\n#### 1. Short title\nThis Act may be cited as the Supreme Court Ethics and Investigations Act .\n#### 2. Establishment of the Office of Ethics Counsel within the Supreme Court of the United States\n##### (a) In general\nChapter 45 of title 28, United States Code, is amended by adding at the end the following:\n678. Office of Ethics Counsel (a) The Office of Ethics Counsel The Chief Justice is authorized to establish an Office of Ethics Counsel within the Supreme Court of the United States\u2014 (1) constituted by one chief ethics counsel who may employ such officers and employees, subject to the provisions of title 5, governing appointments in the competitive service, and the provisions of chapter 51 and subchapter III of chapter 53 of such title relating to classification and General Schedule pay rates; and (2) to advise and provide guidance to justices of the Supreme Court, and their spouses, on matters of judicial ethics, including\u2014 (A) financial disclosure requirements; (B) the acceptance of gifts; (C) political activity; (D) conflicts of interest and recusal; and (E) the unauthorized disclosure of official Court documents. (b) Ethics counsels (1) Staffing and compensation of counsels (A) Chief Ethics Counsel The chief ethics counsel within the Office of Ethics Counsel\u2014 (i) may not be employed by the Court on the date of enactment of this section; (ii) shall be appointed by the Chief Justice; (iii) shall serve not more than two 6-year terms; and (iv) shall receive an annual rate of pay of at least $225,000. (B) Other counsels Any counsel other than the chief ethics counsel within the Office of Ethics Counsel\u2014 (i) may not be employed by the Court on the date of enactment of this section; (ii) shall be appointed by the chief ethics counsel; (iii) shall serve not more than two 6-year terms; and (iv) shall receive an annual rate of pay of at least $180,000. (2) Qualifications Each counsel of the Office of Ethics Counsel shall\u2014 (A) be licensed to practice law in a State or territory of the United States and a member of the bar in good standing; and (B) possess at least 5 years of experience as a practicing attorney. (3) Expertise Each counsel shall be an individual of exceptional public standing who is specifically qualified to serve within the Office of Ethics Counsel by virtue of the individual\u2019s education, training, and experience, as determined by the Chief Justice. (4) Termination of counsels The employment of a counsel may only be terminated by the Chief Justice for cause. (c) Training On a biannual basis, the Office of Ethics Counsel shall provide, and each justice shall take, a training course on the judicial ethics matters described in subsection (a)(2). (d) Report On an annual basis, the chief ethics counsel shall submit to the Committees on the Judiciary of the House of Representatives and of the Senate a report on the ethics advice given by the Office of Ethics Counsel during the previous year, including\u2014 (1) the number of times advice was sought and given; (2) whether the advice was sought by judicial officers or by judicial employees; (3) information about the topics covered by the advice given, including the number of questions related to gifts, financial disclosures, nonpublic information, and political activity; (4) the number and types of mitigation measures that were recommended, including recusal, divestiture, resignation; (5) the number of times advice described in this subsection was not followed by the individual to whom it was given, if known by the Office. (e) Definitions In this section: (1) The term gift means any gratuity, favor, discount, entertainment, hospitality, loan, forbearance, or other item having monetary value. The term includes services as well as gifts of training, transportation, local travel, lodgings and meals, whether provided in-kind, by purchase of a ticket, payment in advance, or reimbursement after the expense has been incurred. (2) The term political activity means political engagements, such as paid speaking events, fundraisers, or donations to political parties, politicians, political action groups, or endorsements of political candidates. .\n##### (b) Clerical amendment\nThe table of contents of chapter 45 of title 28, United States Code, is amended by inserting after the item relating to section 678 the following:\n678. Office of Ethics Counsel. .\n#### 3. Establishment of the Office of Investigative Counsel within the Supreme Court of the United States\n##### (a) In general\nChapter 45 of title 28, United States Code, as amended by this Act, is further amended by adding at the end the following:\n679. Office of Investigative Counsel (a) Office of investigative counsel The Chief Justice is authorized to establish an Office of Investigative Counsel within the Supreme Court of the United States\u2014 (1) constituted by one Chief Investigative Counsel and at least two additional investigative counsels; and (2) to review and investigate ethics complaints against justices arising from their actions or the actions of their spouses and dependents. (b) Investigative counsels (1) Staffing and compensation of counsels (A) Chief investigative counsel The Chief Investigative Counsel\u2014 (i) may not be employed by the court on the date of enactment of this section; (ii) shall be appointed by the Chief Justice; (iii) shall serve not more than one 6-year term; and (iv) shall receive an annual rate of pay of at least $225,000. (B) Additional investigative counsels The investigative counsels\u2014 (i) may not be employed by the court on the date of enactment of this section; (ii) shall be appointed by the Chief Investigative Counsel; (iii) shall serve at the pleasure of the Chief Investigative Counsel; and (iv) shall receive an annual rate of pay of at least $180,000. (C) Qualifications Each investigative counsel of the Office of Investigative Counsel shall\u2014 (i) be licensed to practice law in a State or territory of the United States and a member of the bar in good standing; and (ii) possess at least 7 years of experience as a practicing attorney. (D) Expertise Each investigative counsel and the Chief Investigative Counsel shall be an individual of exceptional public standing who is specifically qualified to serve within the Office of Investigative Counsel by virtue of the individual\u2019s education, training, and experience. (E) Termination of counsels The employment of the Chief Investigative Counsel may only be terminated by the Chief Justice for cause. (2) Subpoena power (A) In general For the discharge of their duties, the Chief Investigative Counsel shall have the authority to issue subpoenas to compel witnesses to appear and testify and to produce books, papers, correspondence, memoranda, documents, or other relevant records. The Chief Investigative Counsel may issue subpoenas requiring the attendance and testimony of witnesses and the production of any evidence relating to any matter under investigation by the Office of Investigative Counsel, which the Office is empowered to investigate by this section. The attendance of witnesses and the production of evidence may be required from any place within the United States at any designated place of hearing within the United States. (B) Failure to obey a subpoena If a person refuses to obey a subpoena issued under subparagraph (A), the Chief Investigative Counsel may apply to a United States district court for an order requiring that person to appear before the Office of Investigative Counsel to give testimony, produce evidence, or both, relating to the matter under investigation. The application may be made within the judicial district where the hearing is conducted or where that person is found, resides, or transacts business. Any failure to obey the order of the court shall be punishable by contempt of court. (C) Service of subpoenas The subpoenas of the Office of Investigative Counsel shall be served in the manner provided for subpoenas issued by a United States district court under the Federal Rules of Civil Procedure for the United States district courts. (D) Service of process All process of any court to which application is made under subparagraph (B) may be served in the judicial district in which the person required to be served resides or may be found. (c) Ethics complaints (1) Filing An ethics complaint against a justice may be filed with the Office of Investigate Counsel by\u2014 (A) the chair or ranking minority member of the Committee on the Judiciary of the House of Representatives or of the Senate; (B) the Majority Leader or Minority Leader of the Senate; or (C) the Speaker or the Minority Leader of the House of Representatives. (2) Review Not later than 60 days after an ethics complaint is filed under paragraph (1), the Office of Investigative Counsel shall review the complaint and determine whether a full investigation is appropriate. In making a determination under this paragraph, the Office shall consider whether the alleged behavior of a justice violates the Code of Conduct of the Supreme Court, the Judicial Code of Conduct, or any applicable law or regulation. Upon making a determination under this paragraph, the chief counsel shall respond to each ethics complaint filed under paragraph (1), regardless of whether the Office of Investigative Counsel determines that an investigation is appropriate. (3) Investigation If the Office determines that a full investigation is appropriate, it shall open the investigation not later than 15 days after making such determination. (4) Reporting (A) In general The Office of Investigative Counsel shall submit to the Chief Justice a report containing its findings and recommendations about an ethics complaint filed under paragraph (2) (including in the case of a complaint with respect to which the Office determines that no violation has occurred), except that in the case of an ethics complaint with respect to which the Chief Justice is the subject, the Office shall deliver such report to the most senior associate justice. (B) Contents A report under subparagraph (A) shall include\u2014 (i) each violation of the Code of Conduct for the Supreme Court committed by the justice who was the subject of the investigation under paragraph (3), including any such violation that arose as a result of the actions of a spouse or dependant of the justice; and (ii) substantive and actionable recommendations from the Office of Investigative Counsel including recusal, divestment and neutralization conflicts of interest, and other remedies. (C) Publication (i) Chief Justice The Chief Justice may, in his sole discretion, release to the public a report received under subparagraph (A), but may not alter such a report in any way, except to redact any classified or personally identifiable information. In the case of an ethics complaint with respect to which the Chief Justice is the subject, the most senior associate justice is authorized to carry out this clause. (ii) Availability to Congress Not later than 10 days after completing a report under subparagraph (A), the Office of Investigative Counsel shall make the report available to\u2014 (I) the Committees on the Judiciary of the House of Representatives and of the Senate; (II) the Committee on Oversight and Government Reform of the House of Representatives; and (III) the Committee on Homeland Security and Governmental Affairs of the Senate. (iii) Duty to inform the Attorney General In carrying out the duties of the Office, the Investigative Counsel shall report expeditiously to the Attorney General whenever the Investigative Counsel has reasonable grounds to believe there has been a violation of Federal criminal law. .\n##### (b) Clerical amendment\nThe table of contents of chapter 45 of title 28, United States Code, is amended by inserting after the item relating to section 678, as added by section 2, the following:\n679. Office of Investigative Counsel. .\n#### 4. Severability\nIf any provision of this Act, or any application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act and the application of this Act to any other person or circumstance shall not be affected.",
      "versionDate": "2026-02-25",
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
        "actionDate": "2026-02-25",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3914",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supreme Court Ethics and Investigations Act",
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
        "name": "Law",
        "updateDate": "2026-04-02T14:28:47Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7692ih.xml"
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
      "title": "Supreme Court Ethics and Investigations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supreme Court Ethics and Investigations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to establish an Office of Ethics Counsel and an Office of Investigative Counsel within the Supreme Court of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:28Z"
    }
  ]
}
```
