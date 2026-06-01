# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3873
- Title: KO Cancer Act
- Congress: 119
- Bill type: HR
- Bill number: 3873
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2025-10-11T08:05:19Z
- Update date including text: 2025-10-11T08:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-10 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3873",
    "number": "3873",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "KO Cancer Act",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:19Z",
    "updateDateIncludingText": "2025-10-11T08:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:05:20Z",
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
          "date": "2025-06-10T14:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "MI"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NM"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NJ"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3873ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3873\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Fitzpatrick (for himself and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase funding for cancer research by the National Cancer Institute to be more in proportion to the mortality rates of cancer.\n#### 1. Short title\nThis Act may be cited as the Knock Out Cancer Act or the KO Cancer Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCancer is one of the leading causes of death in the world and has touched nearly every life, either directly or indirectly.\n**(2)**\nCancer is the cause of nearly 1 out of every 4 deaths in the United States, since 2000 totaling over 15 million American lives.\n**(3)**\nEfforts to increase awareness of cancer symptoms among patients and clinicians would lead to earlier detection and improvements in survival rates.\n**(4)**\nScientific understanding and research lead to innovations in effective treatments, controls, and cures for cancer.\n**(5)**\nThe National Cancer Institute has been a leader in finding medical breakthroughs for treatment and therapies for cancer patients.\n**(6)**\nThrough substantial investment in cancer research, potentially even the tripling of necessary funding, the United States will be best able to address the mortality rates of cancer and the impacts on the patient population.\n#### 3. Increasing NCI budget for cancer research\nTo conduct or support cancer research, there is hereby appropriated, for each of fiscal years 2026 through 2030, to the National Cancer Institute, out of amounts in the Treasury not otherwise appropriated, an amount that is equal to 25 percent of the total amount appropriated to the National Cancer Institute for fiscal year 2022, to remain available until expended. Amounts appropriated pursuant to the preceding sentence shall be in addition to amounts otherwise made available to the National Cancer Institute.\n#### 4. Report to Congress on cancer drug shortages\n##### (a) Study\nThe Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, in collaboration with such other agencies as the Secretary deems necessary, shall study the reasons for cancer drug shortages, including\u2014\n**(1)**\neconomic reasons;\n**(2)**\nsupply chain failures;\n**(3)**\ndelays and other complications relating to\u2014\n**(A)**\nthe development of cancer drugs; and\n**(B)**\nthe approval of such drugs by the Food and Drug Administration; and\n**(4)**\ninsufficient generic drugs and biosimilar biological products.\n##### (b) Report\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall complete the study under subsection (a) and submit a report to the appropriate committees of the Congress on the results of such study.\n**(2) Recommendations**\nThe report under paragraph (1) shall include recommendations for addressing the reasons for cancer drug shortages.",
      "versionDate": "2025-06-10",
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
        "name": "Health",
        "updateDate": "2025-06-27T13:23:40Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3873ih.xml"
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
      "title": "KO Cancer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "KO Cancer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Knock Out Cancer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase funding for cancer research by the National Cancer Institute to be more in proportion to the mortality rates of cancer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T05:48:26Z"
    }
  ]
}
```
