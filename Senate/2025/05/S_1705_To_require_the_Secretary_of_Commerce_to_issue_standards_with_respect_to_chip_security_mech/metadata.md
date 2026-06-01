# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1705?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1705
- Title: Chip Security Act
- Congress: 119
- Bill type: S
- Bill number: 1705
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1705",
    "number": "1705",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Chip Security Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-05-08T19:50:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-08T19:50:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NH"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "WY"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-06-16",
      "state": "HI"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "IN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "DE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MO"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "ND"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NV"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "LA"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NC"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1705is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1705\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of Commerce to issue standards with respect to chip security mechanisms for integrated circuit products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chip Security Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ntechnology developed in the United States should serve as the foundation for the global ecosystem of artificial intelligence to advance the foreign policy and national security objectives of the United States and allies and partners of the United States;\n**(2)**\nthe United States can foster goodwill, strengthen relationships, and support innovative research around the world by providing allies and partners of the United States with advanced computing capabilities;\n**(3)**\nadvanced integrated circuits and computing hardware that is exported from the United States must be protected from diversion, theft, and other unauthorized use or exploitation in order to bolster the competitiveness of the United States and protect the national security of the United States;\n**(4)**\nimplementing chip security mechanisms will improve compliance with the export control laws of the United States, assist allies and partners with guarding computing hardware, and enhance protections from bad actors looking to access, divert, or tamper with advanced integrated circuits and computing hardware; and\n**(5)**\nimplementing chip security mechanisms may help with the detection of smuggling or exploitation of advanced integrated circuits and computing hardware, thereby allowing for increased flexibility in export controls and opening the door for more international partners to receive streamlined and larger shipments of advanced computing hardware.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(2) Chip Security Mechanism**\nThe term chip security mechanism means a software-, firmware-, or hardware-enabled security mechanism or a physical security mechanism.\n**(3) Covered integrated circuit product**\nThe term covered integrated circuit product means\u2014\n**(A)**\nan integrated circuit classified under Export Control Classification Number 3A090 or 3A001.z;\n**(B)**\na computer or other product classified under Export Control Classification Number 4A090 or 4A003.z; or\n**(C)**\nan integrated circuit or computer or a product containing an integrated circuit or computer that is classified under an Export Control Classification Number that is a successor or substantially similar to the numbers listed in subparagraphs (A) and (B).\n**(4) Export**\nThe term export has the meaning given that term in section 1742(3) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(3) ).\n**(5) In-country transfer**\nThe term in-country transfer has the meaning given that term in section 1742(6) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(6) ).\n**(6) Reexport**\nThe term reexport has the meaning given that term in section 1742(9) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(9) ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 4. Requirements for security mechanisms for export of integrated circuit products\n##### (a) Primary requirements for chip security mechanisms\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall require any covered integrated circuit product to be outfitted with chip security mechanisms that implement location verification, using techniques that are feasible and appropriate on such date of enactment, before it is exported, reexported, or in-country transferred to or in a foreign country.\n**(2) Notification requirement**\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall require any person that has received a license or other authorization under the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) to export, reexport, or in-country transfer a covered integrated circuit product to promptly report to the Under Secretary of Industry and Security, if the person obtains credible information that the product\u2014\n**(A)**\nis in a location other than the location specified in the application for the license or other authorization;\n**(B)**\nhas been diverted to a user other than the user specified in the application; or\n**(C)**\nhas been subjected to tampering or an attempt at tampering, including efforts to disable, spoof, manipulate, mislead or circumvent location verification mechanisms or other chip security mechanisms.\n##### (b) Development of secondary requirements for chip security mechanisms\n**(1) Assessment**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary shall, in coordination with the Secretary of Defense\u2014\n**(i)**\nconduct an assessment to identify what additional mechanisms, if any, should be added to the primary chip security mechanisms required under subsection (a)(1)\u2014\n**(I)**\nto enhance compliance with the requirements of the Export Control Reform Act of 2018;\n**(II)**\nto prevent, hinder, and detect the unauthorized use, access, or exploitation of covered integrated circuit products;\n**(III)**\nto identify and monitor smuggling intermediaries; and\n**(IV)**\nto achieve any national security or foreign policy objective of the United States that the Secretary considers appropriate; and\n**(ii)**\nif the Secretary identifies any such mechanism, develop requirements for outfitting covered integrated circuit products with that mechanism.\n**(B) Elements**\nThe assessment required by paragraph (1) shall include\u2014\n**(i)**\nan examination of the feasibility, reliability, and effectiveness of\u2014\n**(I)**\nmethods and strategies that prevent the tampering, disabling, or other manipulating of covered integrated circuit products;\n**(II)**\nworkload verification methods;\n**(III)**\nmethods to modify the functionality of covered integrated circuit products that have been illicitly acquired; and\n**(IV)**\nany other method the Secretary determines appropriate for the prevention of unauthorized use, access, or exploitation of covered integrated circuit products;\n**(ii)**\nan analysis of\u2014\n**(I)**\nthe potential costs associated with implementing each method examined under clause (i), including an analysis of\u2014\n**(aa)**\nthe potential impact of the method on the performance of covered integrated circuit products; and\n**(bb)**\nthe potential for the introduction of new vulnerabilities into the products;\n**(II)**\nthe potential benefits of implementing the methods examined under clause (i), including an analysis of the potential increase\u2014\n**(aa)**\nin compliance of covered integrated circuit products with the requirements of the Export Control Reform Act of 2018; and\n**(bb)**\nin detecting, hindering, and preventing unauthorized use, access, or exploitation of the products; and\n**(III)**\nthe susceptibility of the methods examined under clause (i) to tampering, disabling, or other forms of manipulation; and\n**(iii)**\nan estimate of the expected costs to implement at-scale methods to tamper with, disable, or manipulate a covered integrated circuit product, or otherwise circumvent the methods examined under clause (i).\n**(2) Report to Congress**\n**(A) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary, in coordination with the Secretary of Defense, shall submit to the appropriate congressional committees a report on the results of the assessment required by paragraph (1), including\u2014\n**(i)**\nan identification of the chip security mechanisms, if any, to be included in the requirements for secondary chip security mechanisms; and\n**(ii)**\nif applicable, a roadmap for the timely implementation of the secondary chip security mechanisms.\n**(B) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n**(3) Implementation**\n**(A) In general**\nIf any mechanisms are determined by the Secretary to be appropriate, the Secretary shall, not later than 2 years after the date on which the Secretary completes the assessment required by paragraph (1), require any covered integrated circuit product to be outfitted with the secondary chip security mechanisms identified pursuant to paragraph (1)(A) before the product is exported, reexported, or in-country transferred to or in a foreign country.\n**(B) Privacy**\nIn implementing requirements for secondary chip security mechanisms under subparagraph (A), the Secretary shall prioritize confidentiality.\n##### (c) Enforcement authority\nIn carrying out this section, the Secretary may\u2014\n**(1)**\nverify, in a manner the Secretary determines appropriate, the ownership and location of a covered integrated circuit product that has been exported, reexported, or in-country transferred to or in a foreign country;\n**(2)**\nmaintain a record of covered integrated circuit products and include in the record the location and current end-user of each such product; and\n**(3)**\nrequire any person who has been granted a license or other authorization under the Export Control Reform Act of 2018 to export, reexport, or in-country transfer a covered integrated circuit product to provide the information needed to maintain the record.\n##### (d) Annual assessment and report on new chip security mechanisms\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter for 3 years, the Secretary shall\u2014\n**(1)**\nin coordination with the Secretary of Defense, conduct an assessment of new chip security mechanisms that have been developed in the year preceding the date of the assessment; and\n**(2)**\nsubmit to the appropriate congressional committees a report that includes\u2014\n**(A)**\na summary of the results of the assessment required by paragraph (1);\n**(B)**\nan evaluation of whether any of the new mechanisms assessed under paragraph (1) should be added to or replace any of the existing requirements for secondary chip security mechanisms developed under subsection (b)(1); and\n**(C)**\nany recommendations for modifications to relevant export controls to allow for more flexibility with respect to the countries to or in which covered integrated circuit products may be exported, reexported, or in-country transferred if the products include chip security mechanisms that meet the requirements developed under subsection (b)(1).",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-26",
        "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 0."
      },
      "number": "3447",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Chip Security Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-04-06T20:27:02Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-06T20:27:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-06T20:27:02Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-04-06T20:27:02Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-04-06T20:27:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-06-05T15:03:19Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1705is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Chip Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chip Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Commerce to issue standards with respect to chip security mechanisms for integrated circuit products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:47Z"
    }
  ]
}
```
