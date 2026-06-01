# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6187?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6187
- Title: Wojnovich Pipeline Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6187
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-07T09:05:50Z
- Update date including text: 2026-01-07T09:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-21 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6187",
    "number": "6187",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "Wojnovich Pipeline Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:50Z",
    "updateDateIncludingText": "2026-01-07T09:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-21",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-21T18:24:57Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6187ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6187\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Fitzpatrick (for himself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Administrator of the Pipeline and Hazardous Materials Safety Administration to establish a grant program to facilitate the improved safety and modernization of hazardous liquid distribution infrastructure, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wojnovich Pipeline Safety Act of 2025 .\n#### 2. Hazardous liquid distribution infrastructure safety and modernization grant program\n##### (a) Establishment\nThe Administrator of the Pipeline and Hazardous Materials Safety Administration shall establish a grant program to facilitate the improved safety and modernization of hazardous liquid distribution infrastructure.\n##### (b) Eligible recipients\n**(1) In general**\nThe Secretary may award a grant to\u2014\n**(A)**\na municipality in a State that carries out the disclosures described in section 4; or\n**(B)**\na community-owned utility that is not a for-profit entity in such State.\n**(2) Public-Private partnerships**\nAn eligible recipient described in paragraph (1) may engage in public-private partnerships while carrying out a project using funds provided under this section.\n##### (c) Selection of eligible projects\n**(1) Notice of funding opportunity**\nNot later than 180 days after the date on which funds are made available to carry out the program, the Secretary shall publish a notice of funding opportunity for the funds.\n**(2) Applications**\nThe Secretary shall establish a procedure for awarding grants that takes into consideration\u2014\n**(A)**\nthe risk profile of the existing pipeline system operated by the applicant, including the presence of pipe prone to leakage;\n**(B)**\nthe potential of the project for creating jobs; and\n**(C)**\neconomic impact or growth.\n##### (d) Awards\n**(1) Notice of funding opportunity**\nNot later than 180 days after each date on which the funds to carry out this section are made available, the Secretary shall issue a notice of funding opportunity.\n**(2) Determination**\nNot later than 270 days after issuing a notices of funding opportunity under subparagraph (A), the Secretary shall make awards.\n**(3) Limitation**\nThe Secretary shall award not more than 12.5 percent of the funds available under this program to a single municipality or community-owned utility.\n##### (e) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section $100 million for each of fiscal years 2026 through 2030.\n**(2) Administrative costs**\nNot more than 2 percent of the amounts made available each fiscal year to carry out this section may be used to pay the administrative costs of carrying out the program.\n**(3) Inspector general oversight**\nThe Secretary shall transfer one-half of one percent of the amounts provided to carry out this program in each of fiscal years 2026 through 2030 to the inspector general of the Department of Transportation for oversight of funding provided to the Department of Transportation.\n#### 3. Update website\n##### (a) In general\nThe Secretary of Transportation shall update the website of the Pipeline and Hazardous Materials Safety Administration to increase the ease of use and public accessibility of the website.\n##### (b) Reporting\nIn updating the website under paragraph (1), the Secretary shall require\u2014\n**(1)**\neasily readable reporting of each accident and incident, including information on the details of such accident or incident; and\n**(2)**\nwith respect to each accident or incident, a remediation status update to be provided by operators and posted on the website not less than every 90 days until the remediation is complete.\n#### 4. Public notification and preparedness\n##### (a) Real estate disclosure\n**(1) In general**\nTo be eligible to participate in the grant program established under section 2, a State shall require each real estate contract to include the disclosure of any known hazardous liquid pipeline easements regulated by the Pipeline and Hazardous Materials Safety Administration that are within one-half mile of the boundary of the property subject to such contract.\n**(2) Content**\nThe notice shall include\u2014\n**(A)**\nthe name and contact information of the operator;\n**(B)**\nthe name of the pipeline and the substance in the pipeline;\n**(C)**\nwhether the pipeline has undergone repairs in the 10 years prior to the date of submission of the notice; and\n**(D)**\na list of any leaks, failures, accidents, or incidents the operator has had within the State in the last 10 years.\n**(3) Information availability**\nThe Administrator of the Pipeline and Hazardous Materials Safety Administration shall ensure the information required under paragraph (2) is collected and made publicly available on a website of the Administration.\n##### (b) Emergency response plans\nSection 60102(d)(5) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B) by striking and at the end; and\n**(2)**\nby adding at the end the following:\n(D) a community involvement strategy detailing how the operator will inform and liaise with landowners and homeowners impacted by a release; and .\n##### (c) Emergency alert system\nNot later than 18 months after the date of enactment of this Act, the Secretary shall issue a final rule requiring each operator of a hazardous liquid pipeline facility to\u2014\n**(1)**\nestablish and maintain a localized emergency alert system to send an alert to communities within 1 mile of a pipeline of any leaks, failures, accidents, or incidents; or\n**(2)**\nestablish an agreement with each State in which the operator operates in which such State agrees to use an alert system of the State to send such alert.\n##### (d) Rulemaking\nNot later than 18 months after the date of enactment of this Act, the Secretary shall issue a final rule that requires\u2014\n**(1)**\na standard, timely process or procedure for pipeline operators to conduct in-person tests of water, soil, or air for potential pipeline leaks or failures;\n**(2)**\nin the case of an in-person water test\u2014\n**(A)**\nthe test to be conducted on any well within one-half mile of a leak, accident, incident, or failure; and\n**(B)**\nsamples to be taken from both the top and the bottom of such well;\n**(3)**\nannual in-line inspection tool tests for pipelines older than 50 years or wherever a sleeve repair has been made; and\n**(4)**\nnotifying impacted residents and landowners when a test comes back positive for contaminated water, soil, or air.\n#### 5. Penalty for accident\nThe Secretary shall levy a penalty in the amount of $2,500,000 against an operator of a hazardous liquid pipeline facility that declares a leak, accident, incident, or failure.\n**(1) Frequency**\nThe penalty shall be levied on an annual basis until the Secretary certifies that such leak, accident, incident, or failure has been remediated.\n**(2) Double penalty**\nIn the case of any operator which does not declare a leak, accident, incident, or failure within 15 days of the operator knowing that such a leak, accident, incident, or failure has occurred, the penalty shall be in the amount of $5,000,000.\n#### 6. Emergency reimbursement\n##### (a) In general\nNot later than 30 days after the date on which the Pipeline and Hazardous Materials Safety Administration is provided a declaration by an operator of a hazardous liquid pipeline facility that an event has occurred, the Secretary shall make available funds to reimburse an eligible entity for the following:\n**(1)**\nThe cost of replacing equipment that is damaged, contaminated, or otherwise rendered unusable as a result of the response of the eligible entity to an event.\n**(2)**\nOvertime pay for firefighters, law enforcement officers, or other emergency responders who work at the scene of an event.\n**(3)**\nOperational costs for actions taken to respond to an event.\n**(4)**\nAny other purpose related to an event, as determined by the Secretary of Transportation.\n**(5)**\nTo retroactively cover a cost described in any of paragraphs (1) through (4) that is incurred after the date of an event or within 30 days of the receipt of amounts under this subsection.\n##### (b) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means a State or local emergency response group, including a law enforcement agency, a fire department, and an emergency response agency, located in an area affected by a hazardous train event.\n**(2) Event**\nThe term event means a hazardous liquid pipeline leak, accident, incident, or failure.\n#### 7. Hazardous liquid pipeline community trust fund\n##### (a) In general\nThere is established within the Treasury of the United States a fund which shall be known as the Hazardous Liquid Pipeline Community Trust Fund and which shall be administered by the Secretary of Transportation.\n##### (b) Deposits\nPenalties collected pursuant to section 5 of this Act shall be deposited into the Hazardous Liquid Pipeline Community Trust Fund established in subsection (a).\n##### (c) Disbursement\nThe Secretary shall make disbursements from the Trust Fund to carry out sections 2 and 6 of this Act.\n#### 8. Quarterly report on industry knowledge\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, and quarterly thereafter, the Administrator of the Pipeline and Hazardous Materials Safety Administration shall deliver to the appropriate congressional committees a report which details industry knowledge or developments regarding hazardous liquid pipeline safety and integrity.\n##### (b) Incorporation\nThe Administrator shall make every reasonable effort to incorporate relevant knowledge or developments regarding safety and integrity from each quarterly report into the regulations, guidance, recommendations, advisories, or notices of the Administration.\n#### 9. Office of Public Engagement\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall rename the Community Liaison Services within the Office of Pipeline Safety of the Pipeline and Hazardous Materials Safety Administration as the Office of Public Engagement (in this section referred to as the Office ).\n##### (b) Duties\nThe duties of the Office are to\u2014\n**(1)**\nproactively engage with pipeline stakeholders, including the public, pipeline operators, public safety organizations, and State, local, and Tribal government officials, to raise awareness of pipeline safety practices;\n**(2)**\npromote the adoption and increased use of safety programs and activities;\n**(3)**\ninform the public of pipeline safety regulations and best practices; and\n**(4)**\nassist the public with inquiries regarding pipeline safety.\n##### (c) Public accessibility\nThe Office shall ensure that activities carried out by the Office and information products developed by the Office are accessible to the public.\n##### (d) Community liaisons\n**(1) In general**\nThe Office shall incorporate positions known as community liaisons under the Community Liaison Services.\n**(2) Meeting inclusion**\nFor the purposes of formulating a proposed safety order case, the Administrator shall make every reasonable effort to include a community liaison in each meeting or separately provide the community liaison with a detailed update of each proposed safety order case meeting.\n##### (e) Report\nNot later than 18 months after the date of enactment of this Act, the Secretary shall submit to Congress a report on the implementation of this section.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-05T15:06:17Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6187ih.xml"
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
      "title": "Wojnovich Pipeline Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wojnovich Pipeline Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Pipeline and Hazardous Materials Safety Administration to establish a grant program to facilitate the improved safety and modernization of hazardous liquid distribution infrastructure, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T07:48:31Z"
    }
  ]
}
```
