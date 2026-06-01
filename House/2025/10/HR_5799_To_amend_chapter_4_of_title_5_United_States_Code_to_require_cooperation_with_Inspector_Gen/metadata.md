# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5799
- Title: FALCON Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5799
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2025-12-08T21:16:51Z
- Update date including text: 2025-12-08T21:16:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5799",
    "number": "5799",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FALCON Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-08T21:16:51Z",
    "updateDateIncludingText": "2025-12-08T21:16:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:01:45Z",
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
      "sponsorshipDate": "2025-10-21",
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
      "sponsorshipDate": "2025-10-21",
      "state": "MA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CT"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MD"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "OH"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NM"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "PA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5799ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5799\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Garcia of California (for himself, Ms. Norton , Mr. Lynch , Ms. DeLauro , Mr. Scott of Virginia , Mr. Mfume , Ms. Brown , Ms. Stansbury , Ms. Simon , Mr. Frost , Ms. Lee of Pennsylvania , Mr. Casar , Ms. Crockett , Mr. Min , Mr. Subramanyam , and Ms. Ansari ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend chapter 4 of title 5, United States Code, to require cooperation with Inspector General requests, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fast Action for Lawful Compliance with Oversight Needs Act of 2025 or the FALCON Act of 2025 .\n#### 2. Cooperation with Inspector General requests\n##### (a) In general\nChapter 4 of title 5, United States Code, is amended by adding at the end the following:\n425. Cooperation with Inspector General requests. (a) Requirement To comply with IG requests Any officer or employee of a covered agency (including the head of such agency and any political appointee of such agency), grant recipient of a covered agency (or any subgrantee thereof at any tier), or contractor of a covered agency (or any subcontractor thereof at any tier) that receives a covered request from an Inspector General shall comply with such request not later than 60 days after receiving such request. (b) Appropriate administrative discipline (1) In general Any individual or entity described under subsection (a) that receives a covered request from an Inspector General, and fails to comply with such request in accordance with such subsection, may be subject to appropriate administrative discipline, including as applicable and when circumstances so warrant\u2014 (A) removal or suspension without pay when the circumstance warrants such discipline; or (B) an adverse contract action. (2) Limitation Any discipline under this subsection\u2014 (A) with respect to an officer, employee, grant recipient, subgrantee, contractor, or subcontractor shall be at the sole discretion of the head of the covered agency concerned; and (B) with respect to the head of a covered agency, shall be at the sole discretion of the President. (c) Notification (1) With respect to failure to comply If an individual or entity described under subsection (a) receives a covered request from an Inspector General, and the Inspector General determines that the individual or entity failed to comply with such request in accordance with such subsection, such Inspector General shall, not later than 30 days after making such determination, submit to the appropriate congressional committees and the head of such agency a notification regarding such noncompliance. (2) Contents Each notification required by paragraph (1) shall include the following: (A) With respect to the individual or entity that failed to comply with the request\u2014 (i) the job title of such individual (in the case that the individual is an officer or employee of a covered agency), or the name of the individual or entity (in the case that the individual or entity is a contractor, subcontractor, grantee, or subgrantee); and (ii) the organizational unit of the agency within which the individual or entity works. (B) The date on which the request was initially made. (C) The general subject matter of the information of requested. (3) Form The notification required by paragraph (1) shall be in unclassified form, but may include a classified annex containing additional information relating to the general subject matter of any information requested. (d) Definitions In this section: (1) Covered agency The term covered agency means the following: (A) An establishment. (B) A designated Federal entity. (2) Covered request The term covered request \u2014 (A) means a request for information, access, or assistance under section 406, including an interview or access for documents; and (B) does not include a request for\u2014 (i) access to any information with respect to which Congress has, in accordance with section 406(a)(1)(B), limited the right of access of the Inspector General; (ii) information or assistance under subsection (a)(1) or (a)(3) of section 406 that is, in the judgment of an Inspector General, reasonably refused or not provided; (iii) access to any information or assistance prohibited by\u2014 (I) the Secretary of Defense pursuant to section 408(b)(2); (II) the Secretary of Treasury pursuant to section 412; (III) the Attorney General pursuant to section 413; (IV) the Secretary of Homeland Security pursuant to section 417; or (V) the Secretary of Energy pursuant to section 421; or (iv) grand jury materials\u2014 (I) that are protected from disclosure pursuant to rule 6(e) of the Federal Rules of Criminal Procedure; and (II) with respect to which the Attorney General has not granted the Inspector General access. (3) Inspector General The term Inspector General means an Inspector General of a covered agency. .\n##### (b) Directives\nNot later than 30 days after the date of the enactment of this Act, the head of each covered agency (as such term is defined in section 425 of title 5, United States Code (as added by subsection (a))) shall make explicit in writing to all personnel of the agency (and shall consider updating any agency personnel directives or policies) to specify, that if any of such personnel does not comply within 60 days with a request for an interview or access to documents from the Inspector General of the covered agency in accordance with section 425 of title 5, United Sates Code, such personnel may be subject to appropriate administrative discipline (including, as applicable and when circumstances so warrant, suspension without pay or removal or an adverse contract action) under such section.\n##### (c) Technical amendments\n**(1) Table of contents**\nThe table of sections for chapter 4 of title 5, United States Code, is amended by adding at the end the following:\n425. Cooperation with Inspector General requests. .\n**(2) Definition of appropriate congressional committees**\nSection 401 of title 5, United States Code, is amended\u2014\n**(A)**\nby redesignating paragraphs (1), (2), (3), (4), and (5) as paragraphs (2), (3), (4), (5), and (6), respectively; and\n**(B)**\nby inserting before paragraph (2), as redesignated, the following new paragraph (1):\n(1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Homeland Security and Governmental Affairs of the Senate; (B) the Committee on Oversight and Government Reform of the House of Representatives; and (C) any other relevant congressional committee or subcommittee of jurisdiction. .",
      "versionDate": "2025-10-21",
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
        "actionDate": "2025-10-21",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3026",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FALCON Act",
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
        "updateDate": "2025-12-08T21:15:30Z"
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
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5799ih.xml"
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
      "title": "FALCON Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FALCON Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fast Action for Lawful Compliance with Oversight Needs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T03:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 4 of title 5, United States Code, to require cooperation with Inspector General requests, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-25T03:48:15Z"
    }
  ]
}
```
