# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4712?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4712
- Title: Parity for Tribal Law Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 4712
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-03-06T09:07:01Z
- Update date including text: 2026-03-06T09:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4712",
    "number": "4712",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Parity for Tribal Law Enforcement Act",
    "type": "HR",
    "updateDate": "2026-03-06T09:07:01Z",
    "updateDateIncludingText": "2026-03-06T09:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:15:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:15:00Z",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "OK"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "KS"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MT"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NM"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "WA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "CO"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "ID"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4712ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4712\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Newhouse (for himself, Ms. Perez , Mr. Cole , Ms. Davids of Kansas , Mr. Moolenaar , Ms. Strickland , Mr. Zinke , Mr. Vasquez , Ms. Craig , and Mr. Baumgartner ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Indian Law Enforcement Reform Act to provide for advancements in public safety services to Indian communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parity for Tribal Law Enforcement Act .\n#### 2. Tribal law enforcement officers\nThe Indian Law Enforcement Reform Act is amended by inserting after section 4 ( 25 U.S.C. 2803 ) the following:\n4A. Tribal law enforcement officers (a) In general Notwithstanding any other provision of Federal law, law enforcement officers of an Indian tribe that have contracted or compacted any or all Federal law enforcement functions through a contract or compact entered into pursuant to the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ) (referred to in this section as Tribal officers ) shall have the authority to enforce Federal law within the area under the jurisdiction of the Indian tribe if\u2014 (1) the applicable Tribal officers have\u2014 (A) completed training that is comparable to that of an employee of the Office of Justice Services of the Bureau who is providing the same services in Indian country, as determined by the Deputy Bureau Director of the Office of Justice Services of the Bureau (or a designee); (B) passed an adjudicated background investigation equivalent to that of an employee of the Office of Justice Services of the Bureau who is providing the same services in Indian country; and (C) received a certification from the Office of Justice Services of the Bureau, as described in subsection (c); and (2) the Indian tribe has adopted policies and procedures that meet or exceed those of the Office of Justice Services of the Bureau for the same program, service, function, or activity. (b) Deemed To be Federal law enforcement officers Subject to the guidance issued by the Secretary pursuant to subsection (c)(1)(B) and notwithstanding any other provision of law, while acting under the authority granted by the Secretary through a contract or compact entered into pursuant to the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ), a Tribal officer shall be deemed to be\u2014 (1) a Federal law enforcement officer for the purposes of\u2014 (A) sections 111 and 1114 of title 18, United States Code; (B) chapters 83 and 84 of title 5, United States Code; and (C) chapter 171 of title 28, United States Code (commonly known as the Federal Tort Claims Act ); and (2) an eligible officer under subchapter III of chapter 81 of title 5, United States Code. (c) Certification (1) In general Not later than 2 years after the date of enactment of the Parity for Tribal Law Enforcement Act , the Secretary shall\u2014 (A) notwithstanding section 5, develop procedures for the credentialing of Tribal officers under this section to provide confirmation that Tribal officers meet minimum certification standards and training requirements for Indian country peace officers, as prescribed by the Secretary; and (B) notwithstanding any other provision of law, issue guidance, in consultation with Indian tribes, to otherwise implement this section, ensuring that, in implementing subsection (b)(1)(B), the guidance\u2014 (i) provides for the voluntary participation by Tribal officers, on a position-by-position basis; (ii) allows Tribal officers to purchase service credit for prior years of service consistent with the guidance issued by the Secretary under this subparagraph; (iii) allows for the participation of Tribal officers, the salaries of which are funded in whole or in part by grants from the Office of Community Oriented Policing Services of the Department of Justice or any other agency in the Department of Justice; and (iv) recognizes that Tribal officers may participate if the Indian tribes of those Tribal officers have a mandatory retirement age that exceeds the applicable Federal mandatory retirement age for Federal law enforcement officers. (2) IPA Bridge Program Tribal officers who choose to attend a State or other equivalent training program approved by the Deputy Bureau Director of the Office of Justice Services of the Bureau (or a designee) rather than attend the Indian Police Academy shall be required to attend the Bridge Program of the Indian Police Academy, or an equivalent program, prior to receiving a certification under this subsection. .\n#### 3. Oversight, coordination, and accountability\nThe Attorney General, acting through the Deputy Attorney General, shall coordinate and provide oversight for all Department of Justice activities, responsibilities, functions, and programs to ensure a coordinated approach for public safety in Indian communities, accountability, and compliance with Federal law, including\u2014\n**(1)**\nthe timely submission of reports to Congress;\n**(2)**\nrobust training, as required under Federal law and as needed or requested by Indian Tribes or Federal and State officials relating to\u2014\n**(A)**\npublic safety in Indian communities; and\n**(B)**\ntraining outcomes demonstrating a better understanding of public safety approaches in Indian communities;\n**(3)**\nthe updating of, and improvements to, United States Attorney operational plans;\n**(4)**\ncomprehensive evaluation and analysis of data, including approaches to collecting better data, relating to public safety in Indian communities; and\n**(5)**\nother duties or responsibilities as needed to improve public safety in Indian communities.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "2452",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Parity for Tribal Law Enforcement Act",
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
        "name": "Native Americans",
        "updateDate": "2025-09-16T22:12:44Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4712ih.xml"
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
      "title": "Parity for Tribal Law Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parity for Tribal Law Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Indian Law Enforcement Reform Act to provide for advancements in public safety services to Indian communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:30Z"
    }
  ]
}
```
