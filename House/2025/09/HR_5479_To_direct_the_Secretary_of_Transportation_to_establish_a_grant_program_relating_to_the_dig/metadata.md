# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5479?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5479
- Title: MAP Roads Act
- Congress: 119
- Bill type: HR
- Bill number: 5479
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-19T09:07:17Z
- Update date including text: 2025-12-19T09:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-19 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-19 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5479",
    "number": "5479",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "MAP Roads Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:17Z",
    "updateDateIncludingText": "2025-12-19T09:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-19T21:47:00Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NM"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5479ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5479\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Moore of Utah (for himself, Ms. Hoyle of Oregon , Mr. Hurd of Colorado , and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a grant program relating to the digitization of county roads and creation of publicly accessible road datasets, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing Access to Public Roads Act or MAP Roads Act .\n#### 2. Establishment of county road access and mapping pilot program\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary of Transportation shall establish a pilot grant program to provide grants to States to support rural commerce, increase public safety, and improve public access and navigation by funding the digitization of county roads and the creation of centralized, publicly accessible road datasets.\n##### (b) Application\n**(1) In general**\nTo be eligible to receive a grant under this Act, a State shall submit to the Secretary an application at such time, in such form, and containing such information as the Secretary may require.\n**(2) Priority**\nIn selecting an application for a grant under this Act, the Secretary shall give priority to an application in which the applicant State\u2014\n**(A)**\nidentifies a significant deficiency in digitized county roads within the State;\n**(B)**\ndemonstrates the capacity to administer\u2014\n**(i)**\na subgrant program to distribute funds to counties; and\n**(ii)**\na statewide repository for county road data; and\n**(C)**\nexpresses a commitment to coordinating with counties to create shared geospatial data standards.\n##### (c) Use of funds\n**(1) County activities**\nFunds distributed to counties under this Act may be used to\u2014\n**(A)**\ndigitize official county road records;\n**(B)**\nconvert paper maps or outdated formats to standardized geospatial datasets; and\n**(C)**\ntrain personnel or hire contractors to assist in data creation and conversion.\n**(2) State repository**\nEach participating State department of transportation shall\u2014\n**(A)**\nserve as the centralized data repository for all road data produced by counties under this program;\n**(B)**\nensure that such data\u2014\n**(i)**\nis published on a publicly accessible website;\n**(ii)**\nis organized in a manner that distinguishes between public and private roads;\n**(iii)**\nis compatible with third-party mapping platforms; and\n**(iv)**\nis updated at least annually; and\n**(C)**\nto the maximum extent practicable, coordinate with Federal agencies and mapping authorities to align data formats and metadata.\n##### (d) Reporting requirements\nNot later than 6 months after the establishment of the program under subsection (a), and annually thereafter for 3 years, each State awarded a grant under this section shall submit to the Secretary a report, which shall include, with respect to the period of time since the previous report\u2014\n**(1)**\na list of counties that received a subgrant;\n**(2)**\nthe amount of funding distributed to each county;\n**(3)**\nthe number of miles of county roads digitized under the program;\n**(4)**\nthe status of State repository development and data integration efforts; and\n**(5)**\nany recommendations for improvement or expansion of the program.\n##### (e) Definitions\nIn this Act:\n**(1) County**\nThe term county has meaning given the term in section 101 of title 23, United States Code.\n**(2) County road**\nThe term county road means a public road that is recognized and maintained by a county government.\n**(3) Digitization**\nThe term digitization means the process of converting physical or analog map-based information into standardized electronic formats to produce geospatial data.\n**(4) Geospatial data**\nThe term geospatial data has the meaning given such term in section 752 of the Geospatial Data Act of 2018 ( 43 U.S.C. 2801 ).\n##### (f) Savings clause\nNothing in this Act shall be construed to\u2014\n**(1)**\nconfer any new authority upon a county or State to declare, designate, or assert jurisdiction over a road as a county road where such designation or jurisdiction does not otherwise exist under applicable State or local law;\n**(2)**\nalter, affect, or determine the legal status of any road for purposes of ownership, jurisdiction, or public access; or\n**(3)**\nlimit or expand any existing rights, claims, or defenses related to road ownership, rights-of-way, or public access under Federal, State, or local law.\n##### (g) Rule of construction\nNothing in this Act may be construed to permit the public disclosure of geographic information system data regarding the nature, location, character, or ownership of historic, paleontological, or archaeological resources, that is protected under any other provision of law.\n##### (h) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section $20,000,000 for each of fiscal years 2026 through 2031, to remain available until expended.\n**(2) Administrative expenses**\nOf the funds authorized to be appropriated under paragraph (1), the Secretary may use not more than 2 percent of such funds to administer the program established under subsection (a).\n##### (i) Sunset\nThe authority to make grants under this Act shall terminate on September 30, 2031, unless reauthorized by Congress.",
      "versionDate": "2025-09-18",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-18T18:27:57Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5479ih.xml"
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
      "title": "MAP Roads Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MAP Roads Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing Access to Public Roads Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a grant program relating to the digitization of county roads and creation of publicly accessible road datasets, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:16Z"
    }
  ]
}
```
