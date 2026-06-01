# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4955?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4955
- Title: CLEAN Pacific Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4955
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-10-01T08:06:02Z
- Update date including text: 2025-10-01T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4955",
    "number": "4955",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "CLEAN Pacific Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-01T08:06:02Z",
    "updateDateIncludingText": "2025-10-01T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "HI"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "AS"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "MP"
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
      "sponsorshipDate": "2025-08-26",
      "state": "VA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "HI"
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
      "sponsorshipDate": "2025-09-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4955ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4955\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Moylan (for himself, Mr. Case , Mrs. Radewagen , and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo establish the Pacific Counternarcotics Initiative to assist certain countries with counterdrug interdiction efforts.\n#### 1. Short title\nThis Act may be cited as the Combating Lethal Elements and Narcotics in the Pacific Act of 2025 or the CLEAN Pacific Act of 2025 .\n#### 2. Establishment of the Pacific Counternarcotics Initiative\n##### (a) Establishment\nThe Secretary shall establish a Pacific Counternarcotics Initiative program to assist beneficiary countries with the following:\n**(1)**\nImproving and increasing the rates at which listed chemicals are seized and destroyed.\n**(2)**\nAlleviating the backlog of\u2014\n**(A)**\nlisted chemicals to be destroyed; and\n**(B)**\nhazardous waste, generated by illicit drug trafficking, to be disposed of in an environmentally safe and effective manner.\n**(3)**\nEnsuring that seized listed chemicals are not reintroduced into illicit drug production streams.\n**(4)**\nFreeing up storage space for seized listed chemicals.\n**(5)**\nReducing the environmental impact of listed chemicals and associated waste.\n**(6)**\nPromoting international law enforcement efforts, such as international training and interoperable systems and other shared equipment.\n**(7)**\nImproving the capability of, and infrastructure necessary for, law enforcement to seize and destroy listed chemicals.\n##### (b) Implementation plan\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall submit to the appropriate congressional committees a plan explaining the manner in which the Secretary will implement the Pacific Counternarcotics Initiative program established in subsection (a).\n**(2) Components**\nThe implementation plan required under paragraph (1) shall include the following:\n**(A)**\nA timeline for when assistance to beneficiary countries will begin.\n**(B)**\nA 5-year strategy for each beneficiary country that includes a timeline, budgetary projections, anticipated outcomes, and an overview of objectives.\n**(C)**\nSpecific, measurable benchmarks to track the progress beneficiary countries make towards achieving the outcomes listed under subsection (a).\n**(D)**\nThe roles and responsibilities of each relevant Secretary, their respective department, and any other Federal department or agency in carrying out the Pacific Counternarcotics Initiative program.\n**(E)**\nA plan to address security vulnerabilities and corruption risks, that directly impede the seizure, storage, and destruction of listed chemicals, in each beneficiary country.\n**(F)**\nA plan to update the appropriate congressional committees on the results of the Pacific Counternarcotics Initiative program.\n**(G)**\nAn itemized list, for each beneficiary country, of the law enforcement capabilities the Secretary determines\u2014\n**(i)**\nare necessary within the beneficiary country to achieve the outcomes listed under subsection (a);\n**(ii)**\nare not offered by law enforcement in the beneficiary country; and\n**(iii)**\nthat law enforcement in the beneficiary country are capable of offering.\n**(H)**\nAn itemized list, for each beneficiary country, of the law enforcement capabilities the Secretary determines\u2014\n**(i)**\nare necessary within the beneficiary country to achieve the outcomes listed under subsection (a);\n**(ii)**\nare not offered by law enforcement in the beneficiary country;\n**(iii)**\nthat law enforcement in the beneficiary country are not capable of offering; and\n**(iv)**\nthat the United States is capable of offering to law enforcement in the beneficiary country.\n**(3) Annual progress report**\nNot later than 1 year after the date on which the implementation plan is required to be submitted under paragraph (1), and annually thereafter for 5 years, the Secretary shall submit to the appropriate congressional committees a report on the results of the Pacific Counternarcotics Initiative program from the previous fiscal year, including\u2014\n**(A)**\nthe progress of each beneficiary country participating in such program towards achieving the outcomes listed under subsection (a);\n**(B)**\nwith respect to each beneficiary country participating in such program, compliance with, and progress toward, meeting the benchmarks listed for each such country in the implementation plan; and\n**(C)**\nthe type and quantity of listed chemicals destroyed by each beneficiary country participating in such program from the previous fiscal year.\n#### 3. Funding\nThe Secretary of State shall use amounts otherwise authorized to be appropriated to carry out section 481 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2291 ) to carry out this Act.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committees on the Judiciary of the House of Representatives and the Senate.\n**(2) Beneficiary countries**\n**(A) In general**\nExcept as provided in subparagraph (B), the term beneficiary countries means\u2014\n**(i)**\nthe Cook Islands;\n**(ii)**\nthe Federated States of Micronesia;\n**(iii)**\nthe Republic of Fiji;\n**(iv)**\nFrench Polynesia;\n**(v)**\nthe Republic of Kiribati;\n**(vi)**\nthe Republic of Nauru;\n**(vii)**\nNew Caledonia;\n**(viii)**\nNiue;\n**(ix)**\nthe Republic of Palau;\n**(x)**\nthe Independent State of Papua New Guinea;\n**(xi)**\nthe Republic of Marshall Islands;\n**(xii)**\nthe Independent State of Samoa;\n**(xiii)**\nthe Solomon Islands;\n**(xiv)**\nthe Kingdom of Tonga;\n**(xv)**\nTuvalu; and\n**(xvi)**\nthe Republic of Vanuatu.\n**(B) Updates**\nThe Secretary may add or remove any country from the list under subparagraph (A) after providing written notification of such change to the appropriate congressional committees.\n**(3) Listed Chemical**\nThe term listed chemical has the meaning given such term in section 102 of the Controlled Substances Act ( 21 U.S.C. 802 ).\n**(4) Relevant Secretary**\nThe term relevant Secretary means the Secretary of State, the Secretary of Defense, and the Attorney General.\n**(5) Secretary**\nThe term Secretary means the Secretary of State in consultation with the Secretary of Defense and the Attorney General, except as otherwise specified.\n**(6) Interoperable systems**\nThe term interoperable systems means communications, data sharing, and operational equipment that enables seamless coordination between beneficiary countries and United States law enforcement agencies.",
      "versionDate": "2025-08-12",
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
        "name": "International Affairs",
        "updateDate": "2025-09-18T20:58:07Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4955ih.xml"
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
      "title": "CLEAN Pacific Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAN Pacific Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating Lethal Elements and Narcotics in the Pacific Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Pacific Counternarcotics Initiative to assist certain countries with counterdrug interdiction efforts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:21Z"
    }
  ]
}
```
