# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/892
- Title: Mortgage Rate Reduction Act
- Congress: 119
- Bill type: HR
- Bill number: 892
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-06-03T19:48:34Z
- Update date including text: 2025-06-03T19:48:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/892",
    "number": "892",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Mortgage Rate Reduction Act",
    "type": "HR",
    "updateDate": "2025-06-03T19:48:34Z",
    "updateDateIncludingText": "2025-06-03T19:48:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-05T22:42:24Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:09:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr892ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 892\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Ryan introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the heads of certain agencies to disclose information about loans insured and guaranteed by such agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mortgage Rate Reduction Act .\n#### 2. Sense of the Congress\nIt is the sense of the Congress that\u2014\n**(1)**\nthe Assistant Secretary for the Office of Housing and Federal Housing Commissioner should, acting through the Federal Housing Administration, insure second mortgages under section 203 of the National Housing Act for properties for which the Federal Housing Administration has insured a first mortgage, to facilitate the assumption of such first mortgage by a subsequent purchaser of such property;\n**(2)**\nthe Secretary of Agriculture should guarantee loans for eligible housing under section 502(h) of the Housing Act of 1949 that are second mortgages if the Secretary of Agriculture insures the loan that is the first mortgage against such eligible housing, to facilitate the assumption of such first mortgage by a subsequent purchaser of such eligible housing; and\n**(3)**\nthe Secretary of Veterans Affairs should insure and guarantee real estate housing loans secured by second liens under subchapter I of chapter 37 of title 38, United States Code, if the Secretary of Veterans Affairs insures the first lien against such real estate, to facilitate the assumption of the first mortgage against such real estate by a subsequent purchaser of such real estate.\n#### 3. Insurance for secondary mortgages\n##### (a) Federal Housing Administration\n**(1) In general**\nSection 201(a) of the National Housing Act ( 12 U.S.C. 1707(a) ) is amended\u2014\n**(A)**\nby striking a first mortgage each place it occurs and inserting a first mortgage or second mortgage ; and\n**(B)**\nby striking secured thereby. and inserting the following: secured thereby; and the term second mortgage means, with respect to real estate against which there is a first mortgage that has been insured under section 203, such classes of second liens as are commonly given to secure advances on, or the unpaid purchase price of, real estate, under the laws of the State in which the real estate is located, together with the credit instrument, if any, secured thereby .\n**(2) Conforming amendments**\nSection 203 of the National Housing Act ( 12 U.S.C. 1709 ) is amended by striking first mortgage each place it occurs and inserting first mortgage or second mortgage .\n##### (b) Department of Veterans Affairs\nSection 3703(d)(3) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by striking first lien and inserting first lien or second lien ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(C) A real estate housing loan may only be secured by second lien if the Secretary insures or guarantees the first lien on such real estate. .\n#### 4. Disclosure of information about loans guaranteed and insured\n##### (a) Loans insured by the Federal Housing Administration\nThe Assistant Secretary for the Office of Housing and the Federal Housing Commissioner shall, not later than 1 year after the date of the enactment of this section, publish on a public website a list of all properties for which the Federal Housing Administration has insured a mortgage under section 203 of the National Housing Act that includes the following information for each property insured:\n**(1)**\nThe address of the property against which there is a mortgage insured by the Federal Housing Administration.\n**(2)**\nThe date of the origination of the mortgage that is insured by the Federal Housing Administration.\n##### (b) Loans insured by the Department of Agriculture\nThe Secretary of Agriculture shall, not later than 1 year after the date of the enactment of this section, publish on a public website a list of all properties for which the Department of Agriculture has guaranteed loan under section 502(h) of the Housing Act of 1949 that includes the following information for each loan insured:\n**(1)**\nThe address of the property against which there is a loan guaranteed by the Department of Agriculture.\n**(2)**\nThe date of the origination of the loan that is guaranteed by the Department of Agriculture.\n##### (c) Loans insured by the Secretary of Veterans Affairs\nThe Secretary of Veterans Affairs shall, not later than 1 year after the date of the enactment of this section, publish on a public website a list of all properties for which the Department of Veterans Affairs has insured or guaranteed a housing loan under subchapter I of chapter 37 of part III of title 38, United States Code, that includes the following information for each housing loan insured or guaranteed:\n**(1)**\nThe address of the property against which there is a housing loan insured or guaranteed by the Department of Veterans Affairs.\n**(2)**\nThe date of the origination of the housing loan that is insured or guaranteed by the Department of Veterans Affairs.",
      "versionDate": "2025-01-31",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-04T17:14:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr892",
          "measure-number": "892",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr892v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mortgage Rate Reduction Act</strong></p><p>This bill authorizes the federal guarantee, or insurance, of certain second mortgages. Specifically, this applies to properties with a first mortgage guaranteed by the Federal Housing Administration (FHA) or the Department of Veterans Affairs (VA). For a second mortgage to qualify, the first mortgage on the property must be guaranteed under the same authority.</p><p>The bill also requires the publication of mortgage guarantee information by\u00a0the FHA, VA, and Department of Agriculture. For each mortgage guaranteed, these agencies must publish the address of the property and the date of the loan.</p>"
        },
        "title": "Mortgage Rate Reduction Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr892.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mortgage Rate Reduction Act</strong></p><p>This bill authorizes the federal guarantee, or insurance, of certain second mortgages. Specifically, this applies to properties with a first mortgage guaranteed by the Federal Housing Administration (FHA) or the Department of Veterans Affairs (VA). For a second mortgage to qualify, the first mortgage on the property must be guaranteed under the same authority.</p><p>The bill also requires the publication of mortgage guarantee information by\u00a0the FHA, VA, and Department of Agriculture. For each mortgage guaranteed, these agencies must publish the address of the property and the date of the loan.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr892"
    },
    "title": "Mortgage Rate Reduction Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mortgage Rate Reduction Act</strong></p><p>This bill authorizes the federal guarantee, or insurance, of certain second mortgages. Specifically, this applies to properties with a first mortgage guaranteed by the Federal Housing Administration (FHA) or the Department of Veterans Affairs (VA). For a second mortgage to qualify, the first mortgage on the property must be guaranteed under the same authority.</p><p>The bill also requires the publication of mortgage guarantee information by\u00a0the FHA, VA, and Department of Agriculture. For each mortgage guaranteed, these agencies must publish the address of the property and the date of the loan.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr892"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr892ih.xml"
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
      "title": "Mortgage Rate Reduction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mortgage Rate Reduction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the heads of certain agencies to disclose information about loans insured and guaranteed by such agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:40Z"
    }
  ]
}
```
