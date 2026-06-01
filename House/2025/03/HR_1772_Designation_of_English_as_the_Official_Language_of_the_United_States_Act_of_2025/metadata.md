# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1772?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1772
- Title: Designation of English as the Official Language of the United States Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1772
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-02-10T09:05:53Z
- Update date including text: 2026-02-10T09:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1772",
    "number": "1772",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "A000055",
        "district": "4",
        "firstName": "Robert",
        "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
        "lastName": "Aderholt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Designation of English as the Official Language of the United States Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:53Z",
    "updateDateIncludingText": "2026-02-10T09:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:00:15Z",
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
          "date": "2025-03-03T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AZ"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "AL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "IL"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "FL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "GA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NE"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-07-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "GA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1772ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1772\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Aderholt (for himself, Mr. Norman , Mrs. Harshbarger , Mr. Graves , Mr. Hamadeh of Arizona , Mr. Gosar , Mr. Strong , Mr. Moore of Alabama , Mr. Rogers of Alabama , and Mr. Palmer ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo declare English as the official language of the United States, to establish a uniform English language rule for naturalization, and to avoid misconstructions of the English language texts of the laws of the United States, pursuant to Congress\u2019 powers to provide for the general welfare of the United States and to establish a uniform rule of naturalization under article I, section 8, of the Constitution.\n#### 1. Short title\nThis Act may be cited as the Designation of English as the Official Language of the United States Act of 2025 .\n#### 2. Findings\nThe Congress finds and declares the following:\n**(1)**\nThe United States is composed of individuals from diverse ethnic, cultural, and linguistic backgrounds, and continues to benefit from this rich diversity.\n**(2)**\nThroughout the history of the United States, the common thread binding individuals of differing backgrounds has been the English language.\n**(3)**\nAmong the powers reserved to the States respectively is the power to establish the English language as the official language of the respective States, and otherwise to promote the English language within the respective States, subject to the prohibitions enumerated in the Constitution of the United States and in laws of the respective States.\n**(4)**\nPresident Donald J. Trump signed an Executive order on March 1, 2025 Designating English as the Official Language of The United States.\n#### 3. English as official language of the United States\n##### (a) In general\nTitle 4, United States Code, is amended by adding at the end the following new chapter:\n6 OFFICIAL LANGUAGE 161. Official language of the United States The official language of the United States is English. 162. Preserving and enhancing the role of the official language Representatives of the Federal Government shall have an affirmative obligation to preserve and enhance the role of English as the official language of the Federal Government. Such obligation shall include encouraging greater opportunities for individuals to learn the English language. 163. Official functions of government to be conducted in english (a) Official functions The official functions of the Government of the United States shall be conducted in English. (b) Scope For the purposes of this section, the term United States means the several States and the District of Columbia, and the term official refers to any function that (i) binds the Government, (ii) is required by law, or (iii) is otherwise subject to scrutiny by either the press or the public. (c) Practical effect This section shall apply to all laws, public proceedings, regulations, publications, orders, actions, programs, and policies, but does not apply to\u2014 (1) teaching of languages; (2) requirements under the Individuals with Disabilities Education Act; (3) actions, documents, or policies necessary for national security, international relations, trade, tourism, or commerce; (4) actions or documents that protect the public health and safety; (5) actions or documents that facilitate the activities of the Bureau of the Census in compiling any census of population; (6) actions that protect the rights of victims of crimes or criminal defendants; or (7) using terms of art or phrases from languages other than English. 164. Uniform english language rule for naturalization (a) Uniform language testing standard All citizens should be able to read and understand generally the English language text of the Declaration of Independence, the Constitution, and the laws of the United States made in pursuance of the Constitution. (b) Ceremonies All naturalization ceremonies shall be conducted in English. 165. Rules of construction Nothing in this chapter shall be construed\u2014 (1) to prohibit a Member of Congress or any officer or agent of the Federal Government, while performing official functions, from communicating unofficially through any medium with another person in a language other than English (as long as official functions are performed in English); (2) to limit the preservation or use of Native Alaskan or Native American languages (as defined in the Native American Languages Act); (3) to disparage any language or to discourage any person from learning or using a language; or (4) to be inconsistent with the Constitution of the United States. 166. Standing A person injured by a violation of this chapter may in a civil action (including an action under chapter 151 of title 28) obtain appropriate relief. .\n##### (b) Clerical amendment\nThe table of chapters at the beginning of title 4, United States Code, is amended by inserting after the item relating to chapter 5 the following new item:\nChapter 6. Official Language .\n#### 4. General rules of construction for english language texts of the laws of the United States\n##### (a) In general\nChapter 1 of title 1, United States Code, is amended by adding at the end the following new section:\n9. General rules of construction for laws of the United States (a) English language requirements and workplace policies, whether in the public or private sector, shall be presumptively consistent with the laws of the United States. (b) Any ambiguity in the English language text of the laws of the United States shall be resolved, in accordance with the last two articles of the Bill of Rights, not to deny or disparage rights retained by the people, and to reserve powers to the States respectively, or to the people. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 1 of title 1 is amended by inserting after the item relating to section 8 the following new item:\n9. General rules of construction for laws of the United States. .\n#### 5. Implementing regulations\nThe Secretary of Homeland Security shall, within 180 days after the date of enactment of this Act, issue for public notice and comment a proposed rule for uniform testing of English language ability of candidates for naturalization, based upon the principles that\u2014\n**(1)**\nall citizens should be able to read and understand generally the English language text of the Declaration of Independence, the Constitution, and the laws of the United States which are made in pursuance thereof; and\n**(2)**\nany exceptions to this standard should be limited to extraordinary circumstances, such as asylum.\n#### 6. Effective date\nThe amendments made by sections 3 and 4 shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-03-05",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committees on the Judiciary, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1862",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "English Language Unity Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-21T14:01:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119hr1772",
          "measure-number": "1772",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-03",
          "originChamber": "HOUSE",
          "update-date": "2025-07-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1772v00",
            "update-date": "2025-07-15"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Designation of English as the Official Language of the United States Act of 2025</strong></p><p>This bill establishes English as the official language of the United States.</p><p>The bill specifies that the official functions of government in the United States, including in each state and the District of Columbia, shall be conducted in English. Exceptions to this requirement include (1) actions or documents to protect the public health or safety, (2) actions or documents that protect the rights of victims of crimes or criminal defendants, and (3) requirements under the Individuals with Disabilities Education Act.</p><p>The bill also establishes a framework for implementation and enforcement, including by testing English language ability as part of the naturalization process.</p>"
        },
        "title": "Designation of English as the Official Language of the United States Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1772.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Designation of English as the Official Language of the United States Act of 2025</strong></p><p>This bill establishes English as the official language of the United States.</p><p>The bill specifies that the official functions of government in the United States, including in each state and the District of Columbia, shall be conducted in English. Exceptions to this requirement include (1) actions or documents to protect the public health or safety, (2) actions or documents that protect the rights of victims of crimes or criminal defendants, and (3) requirements under the Individuals with Disabilities Education Act.</p><p>The bill also establishes a framework for implementation and enforcement, including by testing English language ability as part of the naturalization process.</p>",
      "updateDate": "2025-07-15",
      "versionCode": "id119hr1772"
    },
    "title": "Designation of English as the Official Language of the United States Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Designation of English as the Official Language of the United States Act of 2025</strong></p><p>This bill establishes English as the official language of the United States.</p><p>The bill specifies that the official functions of government in the United States, including in each state and the District of Columbia, shall be conducted in English. Exceptions to this requirement include (1) actions or documents to protect the public health or safety, (2) actions or documents that protect the rights of victims of crimes or criminal defendants, and (3) requirements under the Individuals with Disabilities Education Act.</p><p>The bill also establishes a framework for implementation and enforcement, including by testing English language ability as part of the naturalization process.</p>",
      "updateDate": "2025-07-15",
      "versionCode": "id119hr1772"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1772ih.xml"
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
      "title": "Designation of English as the Official Language of the United States Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Designation of English as the Official Language of the United States Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To declare English as the official language of the United States, to establish a uniform English language rule for naturalization, and to avoid misconstructions of the English language texts of the laws of the United States, pursuant to Congress' powers to provide for the general welfare of the United States and to establish a uniform rule of naturalization under article I, section 8, of the Constitution.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:20Z"
    }
  ]
}
```
