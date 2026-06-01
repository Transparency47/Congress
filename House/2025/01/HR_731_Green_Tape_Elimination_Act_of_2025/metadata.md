# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/731
- Title: Green Tape Elimination Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 731
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-12-29T19:35:31Z
- Update date including text: 2025-12-29T19:35:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-24 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/731",
    "number": "731",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Green Tape Elimination Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-29T19:35:31Z",
    "updateDateIncludingText": "2025-12-29T19:35:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-24T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NE"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr731ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 731\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Issa (for himself, Mr. Bacon , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo exempt hazardous fuel reduction activities from certain environmental requirements for a 10-year period.\n#### 1. Short title\nThis Act may be cited as the Green Tape Elimination Act of 2025 .\n#### 2. Exemption of hazardous fuel reduction activities from certain environmental requirements\n##### (a) In general\nDuring the 10-year period beginning on the date of the enactment of this section, a hazardous fuel reduction activity carried out on Federal land\u2014\n**(1)**\nshall not be considered a major Federal action for the purposes of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ); and\n**(2)**\nmay be carried out without regard to the provisions of law specified in subsection (b).\n##### (b) Provisions of law specified\nThe provisions of law specified in this subsection are all Federal laws, regulations, and legal requirements of, deriving from, or related to the subject of the following laws:\n**(1)**\nThe Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ).\n**(2)**\nDivision A of subtitle III of title 54, United States Code (commonly referred to as the National Historic Preservation Act ).\n**(3)**\nThe Migratory Bird Treaty Act ( 16 U.S.C. 703 et seq. ).\n**(4)**\nThe Migratory Bird Conservation Act ( 16 U.S.C. 715 et seq. ).\n##### (c) Clean Air Act amendment\nSection 319 of the Clean Air Act ( 42 U.S.C. 7619 ) is amended by adding at the end the following:\n(c) Certain air quality monitoring data excluded In the event a hazardous fuel reduction activity (as that term is defined in section 2(d) of the Green Tape Elimination Act of 2025) is carried out that the Administrator determines has a significant impact on air quality, the Administrator shall exclude air quality monitoring data that is directly due to such hazardous fuel reduction activity from use in determinations by the Administrator with respect to exceedances or violations of the national ambient air quality standard for any air pollutant. .\n##### (d) Definitions\nIn this section:\n**(1) Hazardous fuel**\nThe term hazardous fuel means any vegetative material that is susceptible to burning, including\u2014\n**(A)**\ntrees;\n**(B)**\ngrasses;\n**(C)**\nshrubs;\n**(D)**\nsagebrush;\n**(E)**\nchaparral; and\n**(F)**\nany dead vegetative material on or near the ground.\n**(2) Hazardous fuel reduction activity**\nThe term hazardous fuel reduction activity means an activity the purpose of which is\u2014\n**(A)**\nthe installation of\u2014\n**(i)**\na natural or manmade change in fuel characteristics that affects fire behavior such that a fire can be more readily controlled (commonly known as a fuel break ); or\n**(ii)**\na natural or constructed barrier used to stop or check a fire or to provide a control line from which to work to stop or check a fire (commonly known as a firebreak ); or\n**(B)**\nto reduce hazardous fuels, including\u2014\n**(i)**\nprescribed fire;\n**(ii)**\nwildland fire use; and\n**(iii)**\nthe use of mechanical methods such as crushing, tractor and hand piling, thinning, pruning, cutting, or otherwise removing hazardous fuels.",
      "versionDate": "2025-01-24",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-01T13:22:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr731",
          "measure-number": "731",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-12-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr731v00",
            "update-date": "2025-12-29"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Green Tape Elimination Act of 2025</strong></p><p>This bill exempts hazardous fuel reduction activities on federal lands from certain environmental and historic preservation regulations. <em>Hazardous fuel\u00a0</em>means any vegetative material that is susceptible to burning, such as trees and grasses. <em>Hazardous fuel reduction activities</em> include installing firebreaks, using prescribed fire, and removing the hazardous fuels.</p><p>First, the bill states that hazardous fuel reduction activities are not to be considered a\u00a0major federal action under the National Environmental Policy Act of 1969 (NEPA) for 10 years.\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, the bill exempts\u00a0such actions from environmental review under\u00a0NEPA during that time period.</p><p>Next, the bill exempts hazardous fuel reduction activities from the Endangered Species Act of 1973, the National Historic Preservation Act, the Migratory Bird Treaty Act, and the Migratory Bird Conservation Act for 10 years.</p><p>The bill also directs the Environmental Protection Agency (EPA) to exclude certain air quality data when determining whether there are exceedances or violations of the national ambient air quality standard for air pollutants. In the event a hazardous fuel reduction activity has a significant impact on air quality, the EPA must exclude that data when making such determination.</p>"
        },
        "title": "Green Tape Elimination Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr731.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Green Tape Elimination Act of 2025</strong></p><p>This bill exempts hazardous fuel reduction activities on federal lands from certain environmental and historic preservation regulations. <em>Hazardous fuel\u00a0</em>means any vegetative material that is susceptible to burning, such as trees and grasses. <em>Hazardous fuel reduction activities</em> include installing firebreaks, using prescribed fire, and removing the hazardous fuels.</p><p>First, the bill states that hazardous fuel reduction activities are not to be considered a\u00a0major federal action under the National Environmental Policy Act of 1969 (NEPA) for 10 years.\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, the bill exempts\u00a0such actions from environmental review under\u00a0NEPA during that time period.</p><p>Next, the bill exempts hazardous fuel reduction activities from the Endangered Species Act of 1973, the National Historic Preservation Act, the Migratory Bird Treaty Act, and the Migratory Bird Conservation Act for 10 years.</p><p>The bill also directs the Environmental Protection Agency (EPA) to exclude certain air quality data when determining whether there are exceedances or violations of the national ambient air quality standard for air pollutants. In the event a hazardous fuel reduction activity has a significant impact on air quality, the EPA must exclude that data when making such determination.</p>",
      "updateDate": "2025-12-29",
      "versionCode": "id119hr731"
    },
    "title": "Green Tape Elimination Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Green Tape Elimination Act of 2025</strong></p><p>This bill exempts hazardous fuel reduction activities on federal lands from certain environmental and historic preservation regulations. <em>Hazardous fuel\u00a0</em>means any vegetative material that is susceptible to burning, such as trees and grasses. <em>Hazardous fuel reduction activities</em> include installing firebreaks, using prescribed fire, and removing the hazardous fuels.</p><p>First, the bill states that hazardous fuel reduction activities are not to be considered a\u00a0major federal action under the National Environmental Policy Act of 1969 (NEPA) for 10 years.\u00a0NEPA requires agencies to identify and evaluate the impacts of major federal actions significantly affecting the quality of the human environment prior to finalizing certain decisions. Thus, the bill exempts\u00a0such actions from environmental review under\u00a0NEPA during that time period.</p><p>Next, the bill exempts hazardous fuel reduction activities from the Endangered Species Act of 1973, the National Historic Preservation Act, the Migratory Bird Treaty Act, and the Migratory Bird Conservation Act for 10 years.</p><p>The bill also directs the Environmental Protection Agency (EPA) to exclude certain air quality data when determining whether there are exceedances or violations of the national ambient air quality standard for air pollutants. In the event a hazardous fuel reduction activity has a significant impact on air quality, the EPA must exclude that data when making such determination.</p>",
      "updateDate": "2025-12-29",
      "versionCode": "id119hr731"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr731ih.xml"
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
      "title": "Green Tape Elimination Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Green Tape Elimination Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To exempt hazardous fuel reduction activities from certain environmental requirements for a 10-year period.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:21Z"
    }
  ]
}
```
