# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7418
- Title: STEADFAST Act
- Congress: 119
- Bill type: HR
- Bill number: 7418
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-05-19T08:05:44Z
- Update date including text: 2026-05-19T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-14 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-14 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7418",
    "number": "7418",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "STEADFAST Act",
    "type": "HR",
    "updateDate": "2026-05-19T08:05:44Z",
    "updateDateIncludingText": "2026-05-19T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 8 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
        "item": [
          {
            "date": "2026-05-14T17:16:12Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-09T17:02:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-09T17:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NC"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7418ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7418\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mrs. Bice (for herself, Ms. Lee of Florida , Mr. McDowell , Mr. Smith of New Jersey , and Mr. Mills ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo convert the program of public financing of presidential election campaigns to a program of providing grants to States for enhancing the security of election systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Tech and Election Administration Defenses For All States and Territories Act or the STEADFAST Act .\n#### 2. Conversion of presidential election campaign funding program to State grant program for election security\n##### (a) Election security program\n**(1) Payments**\nSubtitle H of the Internal Revenue Code of 1985 is amended by adding at the end the following new chapter:\n97 Election Security Program and Fund 9051. Payments to States for election security (a) Authorization of payments The Election Assistance Commission shall establish and operate a program under which the Commission shall make payments to eligible States for activities to promote the security of elections for Federal office by updating voting systems to meet security standards. (b) Eligibility A State is eligible to receive a payment under this chapter if the State submits to the Commission, at such time and in such form as the Commission may require, an application containing the following: (1) A plan for the use of the payment. (2) A certification that the State does not permit noncitizens to vote in any election for public office held in the State. (3) Assurances that the State will submit reports to the Commission, at such frequency as the Commission may require, on the use of the payment. (4) Such other information and assurances as the Commission may require. (c) Use of funds (1) Activities described An eligible State may use a payment received under this chapter for the following: (A) Acquiring voting equipment. (B) Cybersecurity efforts to protect voting systems. (C) Providing physical security for the storage of voting equipment. (D) Modernizing and replacing the components of voting systems. (E) Purchasing and printing paper ballots and implementing security features for protecting paper ballots. (F) Securing and protecting electronic poll books. (2) Prohibition A State may not use the funds provided under a payment received under this chapter to pay any of the following: (A) Costs associated with training for election administrators, other than training in the use of election system equipment. (B) Costs associated with any litigation or for the payment of any judgement. (d) Use of qualified vendors (1) Requirement An eligible State may use a payment received under this chapter to carry out activities through a vendor, but only if the vendor is certified as a qualified vendor by the Commission under paragraph (2). (2) Certification (A) In general The Commission shall certify vendors as qualified vendors for purposes of this chapter in accordance with such criteria as the Commission considers appropriate, except that the Commission may not certify a vendor as a qualified vendor if the vendor directly provided funds to a State or unit of local government to support the administration of an election for Federal office. (B) Deadline Not later than 90 days after the date of the enactment of the Securing Tech and Election Administration Defenses For All States and Territories Act, the Commission shall publish the list of qualified vendors for purposes of this chapter. (e) Priority for certain States In determining the eligible States which will receive payments under this chapter, the Commission shall give priority to States which meet each of the following conditions in carrying out elections for Federal office: (1) The State uses paper ballots which permit voters to verify the vote cast on the ballot and which may serve as a paper trail for purposes of post-election audits. (2) The State uses available resources to ensure that noncitizens are not registered to vote and do not vote in such elections, which may include the Systematic Alien Verification for Entitlements Program administered by the Secretary of Homeland Security and the Social Security Number Verification Service of the Social Security Administration. (3) The State requires a voter to, in order to obtain a ballot at a polling place, provide to an election official any of the following forms of valid photo identification: (A) A valid State-issued motor vehicle driver\u2019s license that includes a photo of the individual and an expiration date. (B) A valid State-issued identification card that includes a photo of the individual and an expiration date. (C) A valid United States passport for the individual. (D) A valid military identification for the individual. (E) A valid identification document issued by a Tribal government that includes a photo of the individual and an expiration date. (F) Any other form of government-issued identification specified by the State as valid photo identification for purposes of this subsection, excluding identification cards provided by an educational institution. (f) Amount of payment (1) Number of registered voters The amount of the payment made to an eligible State under this chapter for a fiscal year shall be equal to the product of\u2014 (A) the aggregate amount made available for payments to eligible States under this chapter for the fiscal year; and (B) the registered voter population proportion for the State (as defined in paragraph (2)). (2) Registered voter population proportion The term registered voter population proportion means, with respect to an eligible State, the amount equal to the quotient of\u2014 (A) the number of individuals who are registered to vote in elections for Federal office held in the State, as determined by the State on the basis of the most recent information available; and (B) the total number of individuals who are registered to vote in elections for Federal office held in all eligible States, as determined by the Commission on the basis of the information determined by the eligible States under subparagraph (A). (g) Report required Each State that receives a payment under this chapter shall provide to the Commission and make available on a publicly accessible website of the State a report detailing\u2014 (1) how such payment was spent; and (2) the extent to which the State complied with or deviated from the information submitted in the application described in subsection (b). 9052. Election Security Fund (a) Establishment; purpose (1) In general There is hereby established on the books of the Treasury of the United States a special fund to be known as the Election Security Fund , which shall be used to carry out the program under this chapter. (2) Limit on administrative expenses The Commission may use not more than 5 percent of the amount in the Fund during a fiscal year for the administrative expenses of the Fund during the fiscal year. (b) Funds designated by individual taxpayers The Secretary of the Treasury shall, from time to time, transfer to the fund an amount not in excess of the sum of the amounts designated to the fund by individuals under section 6096. (c) Appropriation There is appropriated to the Fund for each fiscal year, out of amounts in the general fund of the Treasury not otherwise appropriated, an amount equal to the amounts so designated during each fiscal year, which shall remain available to the Fund without fiscal year limitation. 9053. Public information on Program and Fund (a) Providing information to public The Commission shall provide information to the public on the program established under this chapter and the use of the designation of income tax payments under section 6096 of the Internal Revenue Code of 1986 to transfer amounts to the Election Security Fund, including by establishing and operating a hyperlink to such information on the Commission\u2019s official public website. (b) Deadline The Commission shall meet the requirements of subsection (a) not later than 180 days after the date of the enactment of the Securing Tech and Election Administration Defenses For All States and Territories Act. 9054. Definitions In this chapter\u2014 (1) the term Commission means the Election Assistance Commission; (2) the term Fund means the Election Security Fund established under section 9052; and (3) the term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands. .\n**(2) Clerical amendment**\nThe table of sections for subtitle H of such Code is amended by adding at the end the following:\nChapter 97\u2014Election Security Program and Fund Sec. 9051. Payments to States for election security. Sec. 9052. Election Security Fund. Sec. 9053. Public information on Program and Fund. Sec. 9054. Definitions. .\n##### (b) Designation of income tax payments to Election Security Fund\n**(1) Designation**\nSection 6096(a) of such Code is amended by striking the Presidential Election Campaign Fund and inserting the Election Security Fund .\n**(2) Reference to EAC website with public information on Program and Fund**\nSection 6096(a) of such Code is amended by adding at the end the following new sentence: The Secretary shall ensure that the individual tax return form includes a citation to the hyperlink on the official public website of the Election Assistance Commission which is established and operated under section 9053. .\n**(3) Effective date**\nThe amendment made by subsection (a) shall apply with respect to taxable years ending after December 31, 2025.\n#### 3. Termination of taxpayer financing of presidential election campaigns\n##### (a) Termination of Presidential Election Campaign Fund\n**(1) Termination**\nChapter 95 of subtitle H of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9014. Termination The provisions of this chapter shall not apply with respect to any presidential election (or any presidential nominating convention) after the date of the enactment of this section, or to any candidate in such an election. .\n**(2) Clerical amendment**\nThe table of sections for chapter 95 of subtitle H of such Code is amended by adding at the end the following new item:\nSec. 9014. Termination. .\n##### (b) Termination of Presidential Primary Matching Payment Account\n**(1) Termination**\nChapter 96 of subtitle H of such Code is amended by adding at the end the following new section:\n9043. Termination The provisions of this chapter shall not apply to any candidate with respect to any presidential election after the date of the enactment of this section. .\n**(2) Clerical amendment**\nThe table of sections for chapter 96 of subtitle H of such Code is amended by adding at the end the following new item:\nSec. 9043. Termination. .\n##### (c) Transfer of remaining funds to Election Security Fund\nSection 9006 of such Code is amended by adding at the end the following new subsection:\n(d) Transfer of funds remaining after termination The Secretary shall transfer the amounts in the fund as of the date of the enactment of this subsection to the Election Security Fund under section 9052, to be available as described in such section. .",
      "versionDate": "2026-02-09",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-13T16:38:52Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7418ih.xml"
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
      "title": "STEADFAST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STEADFAST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Tech and Election Administration Defenses For All States and Territories Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To convert the program of public financing of presidential election campaigns to a program of providing grants to States for enhancing the security of election systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:43Z"
    }
  ]
}
```
