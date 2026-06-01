# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1740?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1740
- Title: Default Proceed Sale Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 1740
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-03T19:16:33Z
- Update date including text: 2026-04-03T19:16:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1740",
    "number": "1740",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Default Proceed Sale Transparency Act",
    "type": "HR",
    "updateDate": "2026-04-03T19:16:33Z",
    "updateDateIncludingText": "2026-04-03T19:16:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:14:25Z",
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
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1740ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1740\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Schneider (for himself, Mr. Quigley , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo improve the procedures of the national instant criminal background check system in the case of firearm transfers by federally licensed firearms importers, manufacturers, and dealers before the completion of the related criminal background check, and to provide for annual reports on default firearm transfers.\n#### 1. Short title\nThis Act may be cited as the Default Proceed Sale Transparency Act .\n#### 2. Improvement of NICS procedures in the case of default firearm transfers\n##### (a) Requirement that federally licensed firearm importers, manufacturers, and dealers report default firearm transfers\n**(1) In general**\nSection 922(t) of title 18, United States Code, is amended by adding at the end the following:\n(7) A licensed importer, licensed manufacturer, or licensed dealer who transfers a firearm in compliance with paragraph (1), but before the national instant criminal background check system provides the licensee with a unique identification number, shall report the transfer to the Federal Bureau of Investigation within 24 hours. If a State or local law enforcement authority is conducting the related background check, the Federal Bureau of Investigation shall transmit the report to that authority. .\n**(2) Creation of online portal and telephone hotline**\nWithin 180 days after the date of the enactment of this Act, the Attorney General shall create an online portal and telephone hotline, that are to be used exclusively for the purpose of reporting sufficient information to allow the Federal Bureau of Investigation to prioritize background checks in accordance with section 40901 of title 34, United States Code.\n##### (b) Prioritization of NICS background checks relating to default firearm transfers\nSection 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) is amended by adding at the end the following:\n(m) Prioritization of background checks related to default firearm transfers In the case of a transfer referred to in section 922(t)(7) of title 18, United States Code, the system established under this section shall give priority to completing the background check relating to the transfer. .\n##### (c) Prohibition on destruction of records relating to firearm transfer before completion of background check\nSection 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ), as amended by subsection (b) of this section, is amended by adding at the end the following:\n(n) Prohibition on destruction of records relating to firearm transfer before completion of related background check The system established under this section may not destroy any records of the system relating to a proposed or completed firearm transfer, before completion of the criminal background check with respect to the prospective or actual transferee. .\n#### 3. Annual reports on default firearm transfers\n##### (a) In general\nWithin 300 days after the date of the enactment of this Act and annually thereafter, the Director of the Federal Bureau of Investigation shall make accessible to the public a written report on\u2014\n**(1)**\nthe number of firearms transferred as described in section 922(t)(7) of title 18, United States Code, during the period covered by the report, disaggregated by State;\n**(2)**\nthe number of the firearms described in paragraph (1) of this subsection with respect to which the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act completed the background check;\n**(3)**\nof the number described by paragraph (2) of this subsection\u2014\n**(A)**\nthe number with respect to which the system provided the unique identification number under subparagraph (B)(i) or (C)(i) of section 922(t)(1) of such title;\n**(B)**\nthe number with respect to which information available to the system demonstrated that transfer of a firearm to, or receipt of a firearm by, the transferee would violate subsection (d), (g), or (n) of section 922 of such title or State, local, or tribal law; and\n**(C)**\nin each case described by subparagraph (B) of this paragraph, the reason for indicating that the receipt would be a violation referred to in such subparagraph (B), including any specific prohibiting criteria that would bar the transferee from receipt of a firearm or a licensee from transferring a firearm;\n**(4)**\nof the number described by paragraph (3)(B) of this subsection, the number of firearms that were retrieved from the transferee, and the number of firearms that were not retrieved from the transferee, with each number disaggregated by the field division of the Bureau of Alcohol, Tobacco, Firearms and Explosives and the State involved;\n**(5)**\nin the case of the first report under this section, the number of requests for criminal background checks received by the system in the preceding 5 years the records of which were purged from the system without resolution; and\n**(6)**\nthe number of licensed importers, licensed manufacturers, or licensed dealers who transferred firearms as described in section 922(t)(7) of such title during the period covered by the report, disaggregated by the State of sale.\n##### (b) In general\nWithin 300 days after the date of the enactment of this Act and annually thereafter, the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives shall make accessible to the public a written report on\u2014\n**(1)**\nthe average time between receipt and recovery of a firearm transferred as described in section 922(t)(7) of title 18, United States Code, during the period covered by the report, where the transfer to, or receipt by, the transferee violated subsection (d), (g), or (n) of section 922 of such title or State, local, or tribal law;\n**(2)**\nthe number of firearms transferred as described in such section 922(t)(7) during the period covered by the report, that were recovered as part of a criminal investigation, where receipt by the transferee violated such subsection (d), (g), or (n) or State, local, or tribal law, disaggregated by State; and\n**(3)**\nof the number described by paragraph (2) of this subsection\u2014\n**(A)**\nthe total number of firearms that were recovered by law enforcement in States other than the State the firearm was transferred by a licensed importer, licensed manufacturer, or licensed dealer as described in such section 922(t); and\n**(B)**\nthe information outlined in subparagraph (A) of this paragraph, disaggregated by\u2014\n**(i)**\nthe State where the firearm was recovered; and\n**(ii)**\nthe State where the firearm was transferred as described in such section 922(t).\n##### (c) Rule of interpretation\nA report under subsection (a) shall be considered an annual statistical report and statistical aggregate data for purposes of the sixth proviso under the heading Bureau of Alcohol, Tobacco, Firearms and Explosives\u2014salaries and expenses in the Department of Justice Appropriations Act, 2012 (title II of division B of Public Law 112\u201355 ).",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Business records",
            "updateDate": "2025-09-02T19:16:20Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-02T19:16:00Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-09-02T19:15:43Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-02T19:15:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-02T19:16:14Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-02T19:15:38Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-09-02T19:15:49Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-09-02T19:15:55Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-09-02T19:16:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T16:56:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1740",
          "measure-number": "1740",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1740v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Default Proceed Sale Transparency Act</strong></p><p>This bill establishes new requirements in the case of a firearm transfer by a federally licensed dealer, manufacturer, or importer to an unlicensed person prior to the completion of a background check. Current law permits these transactions\u2014default-proceed\u00a0transactions\u2014if a submitted background check remains incomplete after three business days.</p><p>With respect to a default-proceed transaction, the bill</p><ul><li>requires a federally licensed dealer, manufacturer, or importer to report the transfer to the Federal Bureau of Investigation (FBI) within 24 hours;</li><li>requires the National Instant Criminal Background Check System (NICS) to prioritize completing the background check related to the transfer; and</li><li>requires the NICS to retain records related to a proposed or completed firearm transfer until the background check is complete.</li></ul><p>Finally, the bill requires the FBI to report publicly on data related to default-proceed transactions. Further, it requires the Bureau of Alcohol, Tobacco, Firearms and Explosives to report publicly on data related to the firearms transferred in default-proceed transactions.</p>"
        },
        "title": "Default Proceed Sale Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1740.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Default Proceed Sale Transparency Act</strong></p><p>This bill establishes new requirements in the case of a firearm transfer by a federally licensed dealer, manufacturer, or importer to an unlicensed person prior to the completion of a background check. Current law permits these transactions\u2014default-proceed\u00a0transactions\u2014if a submitted background check remains incomplete after three business days.</p><p>With respect to a default-proceed transaction, the bill</p><ul><li>requires a federally licensed dealer, manufacturer, or importer to report the transfer to the Federal Bureau of Investigation (FBI) within 24 hours;</li><li>requires the National Instant Criminal Background Check System (NICS) to prioritize completing the background check related to the transfer; and</li><li>requires the NICS to retain records related to a proposed or completed firearm transfer until the background check is complete.</li></ul><p>Finally, the bill requires the FBI to report publicly on data related to default-proceed transactions. Further, it requires the Bureau of Alcohol, Tobacco, Firearms and Explosives to report publicly on data related to the firearms transferred in default-proceed transactions.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1740"
    },
    "title": "Default Proceed Sale Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Default Proceed Sale Transparency Act</strong></p><p>This bill establishes new requirements in the case of a firearm transfer by a federally licensed dealer, manufacturer, or importer to an unlicensed person prior to the completion of a background check. Current law permits these transactions\u2014default-proceed\u00a0transactions\u2014if a submitted background check remains incomplete after three business days.</p><p>With respect to a default-proceed transaction, the bill</p><ul><li>requires a federally licensed dealer, manufacturer, or importer to report the transfer to the Federal Bureau of Investigation (FBI) within 24 hours;</li><li>requires the National Instant Criminal Background Check System (NICS) to prioritize completing the background check related to the transfer; and</li><li>requires the NICS to retain records related to a proposed or completed firearm transfer until the background check is complete.</li></ul><p>Finally, the bill requires the FBI to report publicly on data related to default-proceed transactions. Further, it requires the Bureau of Alcohol, Tobacco, Firearms and Explosives to report publicly on data related to the firearms transferred in default-proceed transactions.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1740"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1740ih.xml"
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
      "title": "Default Proceed Sale Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Default Proceed Sale Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the procedures of the national instant criminal background check system in the case of firearm transfers by federally licensed firearms importers, manufacturers, and dealers before the completion of the related criminal background check, and to provide for annual reports on default firearm transfers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:52Z"
    }
  ]
}
```
