# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7247
- Title: Prison Libraries Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7247
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-13T08:06:19Z
- Update date including text: 2026-05-13T08:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7247",
    "number": "7247",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Prison Libraries Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:19Z",
    "updateDateIncludingText": "2026-05-13T08:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:31:00Z",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "OH"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NC"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "GA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "HI"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "LA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MS"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NJ"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
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
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "TX"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "WA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "WA"
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
      "sponsorshipDate": "2026-01-27",
      "state": "DC"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "NE"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "WI"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "DE"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7247ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7247\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Cleaver (for himself, Ms. Brown , Mrs. Foushee , Ms. Sewell , Ms. Simon , Mrs. Cherfilus-McCormick , Mr. Johnson of Georgia , Mr. David Scott of Georgia , Mr. Case , Mr. Garc\u00eda of Illinois , Mr. Fields , Ms. Tlaib , Mr. Thanedar , Mr. Thompson of Mississippi , Mrs. McIver , Mr. Evans of Pennsylvania , Ms. Lee of Pennsylvania , Ms. Crockett , Ms. Johnson of Texas , Ms. DelBene , Ms. Randall , and Ms. Norton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a program to make grants for the establishment of prison libraries.\n#### 1. Short title\nThis Act may be cited as the Prison Libraries Act of 2026 .\n#### 2. Establishment\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall establish a program to make grants to eligible applicants for the purpose of providing library services to incarcerated individuals in order to advance reintegration efforts, reduce recidivism, and increase educational opportunities.\n#### 3. Eligibility criteria\nAn eligible grantee under this Act is any State or territory that submits an application that includes the following:\n**(1)**\nA comprehensive plan for how the grant will be used, including project objectives, program design, and evaluation process.\n**(2)**\nProof of the existence of a physical library at a correctional facility or the intention of creating one.\n**(3)**\nData on the demographics of the population of the facility sufficient to demonstrate a compelling need for funding, including educational level of prison population, rates of recidivism, socioeconomic breakdown of the prison population or any other relevant data.\n#### 4. Use of funds\nGrant amounts shall be used to provide library services to incarcerated individuals as set forth in section 2, and may include usage for any of the following:\n**(1)**\nEducation and job training.\n**(2)**\nAcquisition of modern materials and equipment that reflect the interests, identities, abilities, and languages of the prison population.\n**(3)**\nExpansion of the infrastructure of prison libraries to be less restrictive, safety permitted, and more welcoming with design and decor.\n**(4)**\nHiring of qualified librarians and staff to manage the libraries, their resources, and services and serve as the social coordinator for organized activities and events, and who hold the following qualifications:\n**(A)**\nHave practical library management experience.\n**(B)**\nDemonstrated ability to catalogue, archive, and maintain databases and E-resources.\n**(C)**\nDemonstrated ability to organize weekly, bi-weekly, and monthly events and activities.\n**(5)**\nLiterary training.\n**(6)**\nDigital literacy training.\n**(7)**\nCareer readiness programming.\n**(8)**\nCivic engagement programs.\n**(9)**\nRestorative justice programs.\n**(10)**\nResident led programs.\n**(11)**\nHealth and wellness activities.\n**(12)**\nCultural exchange and appreciation programs, events, and activities.\n**(13)**\nComputer (including laptops) and internet access.\n**(14)**\nBook discussion programs.\n**(15)**\nLanguage services, including free English classes.\n**(16)**\nAudiobooks and accessible reading materials for the visually impaired and print disabled.\n**(17)**\neBooks.\n**(18)**\nManagement of book donation programs.\n**(19)**\nAudio and visual materials or multimedia.\n**(20)**\nArtistic programing such as painting, creative writing, poetry slams, drama, or music.\n**(21)**\nFinancial literacy.\n**(22)**\nFamily literacy activities facilitated during in-person visits.\n**(23)**\nResource fairs.\n**(24)**\nMaking reasonable efforts towards building a working relationship with local public libraries, including\u2014\n**(A)**\nadoption of a standardized guideline for library management;\n**(B)**\nsharing of resources and materials through an interlibrary loan arrangement; and\n**(C)**\nimplementation of coordinated organized events and activities.\n#### 5. Prohibited uses\nGrant amounts may not be used for the following:\n**(1)**\nPurchasing food, clothes, shoes, or hygiene supplies.\n**(2)**\nPayment of employee salary and benefits unassociated with prison libraries.\n**(3)**\nPhysical and mental care for incarcerated individuals.\n**(4)**\nIncarcerated individual transportation.\n**(5)**\nStaff training unrelated to the library services.\n**(6)**\nGeneral administrative functions or operations of the prison.\n**(7)**\nFacility maintenance aside from the libraries.\n**(8)**\nOther obligations imposed on the facility by law, including establishment of maintenance of a law library.\n**(9)**\nAny other use unrelated to library services, resources, and management.\n#### 6. Prioritization\nThe Attorney General shall, in making grants under this Act, comply with the following:\n**(1)**\nThe Attorney General shall prioritize making awards to grantees that are the following:\n**(A)**\nApplicants that follow local and or national standards and guidelines for library management.\n**(B)**\nApplicants that add or prioritize post-secondary education curriculum to library programming.\n**(C)**\nApplicants with plans for tangible, positive, and measurable impact for their prison population, including\u2014\n**(i)**\nplans for increasing literacy rates;\n**(ii)**\nplans for increased secondary and post-secondary enrollment and graduation rates;\n**(iii)**\nplans for development of technical and vocational skills;\n**(iv)**\nplans for expanded access to employment opportunities post-release; and\n**(v)**\nany other factors that the Attorney General determines appropriate.\n**(D)**\nApplicants with plans for numerous initiatives to maximize benefits and services for their prison population.\n**(2)**\nThe Attorney General shall ensure geographic diversity as between grantees with regard to the States and territories and between urban and rural areas.\n**(3)**\nThe Attorney General shall establish a reporting system to monitor progress, performance, and expenditures of grantees.\n#### 7. Term\nA grant under this Act shall be for term of one year, and may be renewed annually for a period of not more than 6 years in total.\n#### 8. Reporting\nGrantees shall submit annual performance measures, including library activity statistics and program outcomes, and expenditure reports to systems established by the Attorney General under section 6(4).\n#### 9. Conditions\n##### (a) In general\nA grantee may not charge a fee to any incarcerated individual for the following:\n**(1)**\nAccess to physical books.\n**(2)**\nAccess to eBook and audiobooks.\n**(3)**\nAccess to computers (including laptops) and the internet within the library.\n**(4)**\nAccess to educational and artistic materials needed to facilitate learning, training, and or activities, including notebooks, pens, pencils, paints, and similar supplies.\n**(5)**\nPrinting services.\n**(6)**\nAny other library services or resources.\n##### (b) Availability for educational programming\nA grantee shall make the library space available to post-secondary organizations and personnel for educational programming.\n#### 10. Consultation\nThe Attorney General shall consult with the Director of the Institute of Museum and Library Services in implementing this Act.\n#### 11. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act $10,000,000 for each of fiscal years 2026 through 2031.",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-04-16",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "4320",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prison Libraries Act of 2026",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-13T17:30:46Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7247ih.xml"
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
      "title": "Prison Libraries Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prison Libraries Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a program to make grants for the establishment of prison libraries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:30Z"
    }
  ]
}
```
