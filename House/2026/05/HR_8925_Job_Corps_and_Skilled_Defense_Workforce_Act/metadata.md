# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8925
- Title: Job Corps and Skilled Defense Workforce Act
- Congress: 119
- Bill type: HR
- Bill number: 8925
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-30T08:06:07Z
- Update date including text: 2026-05-30T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8925",
    "number": "8925",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001069",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Courtney, Joe [D-CT-2]",
        "lastName": "Courtney",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Job Corps and Skilled Defense Workforce Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:07Z",
    "updateDateIncludingText": "2026-05-30T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-20T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "MS"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "VA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "GA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "NH"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NE"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "SC"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "KY"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "UT"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "WI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "PA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8925ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8925\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2026 Mr. Courtney (for himself, Mr. Ezell , Mrs. Kiggans of Virginia , Mr. Bishop , Mr. Lawler , Mr. Deluzio , Ms. Tenney , Ms. Goodlander , Mr. Rutherford , Mr. Bacon , Mr. Wilson of South Carolina , Mr. Guthrie , Mr. Moore of Utah , Mr. Grothman , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Defense to align the Job Corps program with the defense industrial base, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Job Corps and Skilled Defense Workforce Act .\n#### 2. Alignment of Job Corps with the defense industrial base\n##### (a) In general\nThe Secretary of Defense, acting through the National Imperative for Industrial Skills program of the Department of Defense (or a successor program), shall\u2014\n**(1)**\nensure that military recruits who are ineligible for enlistment as a result of the requirements of section 520 of title 10, United States Code, are made aware of opportunities to enroll in the Job Corps program authorized under subtitle C of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3191 et seq. ) to receive training that\u2014\n**(A)**\nprepares enrollees for employment as skilled industrial workers in the defense industrial base in the State or local area in which a Job Corps center is located and, to the extent practicable, in the State or local area in which enrollees intend to seek employment after graduation; and\n**(B)**\nincludes programs of advanced career training described in section 148(c) of the Workforce Innovation and Opportunity Act ( 20 U.S.C. 3198(c) ) at existing Job Corps centers or at new Job Corps centers in close proximity to a shipyard or other defense industrial base suppliers; and\n**(2)**\naddress shortages of skilled industrial workers in the defense industrial base by supporting the Job Corps program in offering training that aligns with the needs of the defense industrial base, including through investments in curricula development, equipment, and facilities.\n##### (b) Extension of shipbuilding workforce development special incentive to job corps\n**(1)**\nSection 8696(b)(2) of title 10, United States Code is amended by adding at the end the following:\n(G) The Job Corps program authorized under subtitle C of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3191 et seq. ) or an operator of a Job Corps center described in section 147 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3197 ). .\n**(2)**\nSection 8696(c)(2) of title 10, United States Code, is amended by adding at the end the following:\n(H) The Job Corps program authorized under subtitle C of title I of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3191 et seq. ). .\n##### (c) Job corps conforming reforms\nSection 158(f) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3208 ) is amended\u2014\n**(1)**\nby striking may accept on behalf of the Job Corps or individual Job Corps centers charitable donations of cash and inserting (or the Secretary of Agriculture, as appropriate) on behalf of the Job Corps, or individual Job Corps Center, on behalf of such center, may accept grants, charitable donations of cash , ; and\n**(2)**\nby inserting at the end the following: Notwithstanding sections 501(b) and 522 of title 40, United States Code, any property acquired by a Job Corps center shall be directly transferred, on a nonreimbursable basis, to the Secretary. .\n##### (d) Operations\n**(1) Local authority to realign trades**\nSection 151 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3201 ) is amended by adding at the end the following:\n(d) Local authority Subject to the limitations of the budget approved by the Secretary for a Job Corps center, the operator of a Job Corps center shall have the authority, without prior approval from the Secretary, to\u2014 (1) hire staff and provide staff professional development; (2) set terms and enter into agreements with Federal, State, or local educational partners, such as secondary schools, institutions of higher education, child development centers, units of Junior Reserve Officer Training Corps programs established under section 2031 of title 10, United States Code, or employers; and (3) engage with and educate stakeholders (including eligible applicants for the Job Corps) about Job Corps operations, selection procedures, and activities. .\n**(2) Streamlined enrollment of veterans and military recruits into the defense industrial base**\nSection 144(b) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3194(b) ) is amended\u2014\n**(A)**\nin the heading, by inserting and certain other armed forces members after veterans ; and\n**(B)**\nby inserting or a member of the Armed Forces eligible for preseparation counseling under section 1142 of title 10, United States Code after a veteran .",
      "versionDate": "2026-05-20",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-28T22:29:53Z"
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
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8925ih.xml"
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
      "title": "Job Corps and Skilled Defense Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T02:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Job Corps and Skilled Defense Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Defense to align the Job Corps program with the defense industrial base, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:33Z"
    }
  ]
}
```
