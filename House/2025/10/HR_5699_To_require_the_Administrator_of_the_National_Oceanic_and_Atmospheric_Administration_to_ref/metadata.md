# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5699?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5699
- Title: Fisheries Data Modernization and Accuracy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5699
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2026-04-08T13:28:50Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held
- Latest action: 2025-10-06: Introduced in House

## Actions

- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-11-12 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-11-19 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5699",
    "number": "5699",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "R000609",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. Rutherford, John H. [R-FL-5]",
        "lastName": "Rutherford",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Fisheries Data Modernization and Accuracy Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T13:28:50Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-06",
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
          "date": "2025-10-06T19:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-11-19T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-12T21:44:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MS"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "LA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "GA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "SC"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "TX"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NC"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5699ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5699\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. Rutherford introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Administrator of the National Oceanic and Atmospheric Administration to reform the Marine Recreational Information Program of the National Marine Fisheries Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fisheries Data Modernization and Accuracy Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the National Oceanic and Atmospheric Administration, acting through the Director of the National Marine Fisheries Service.\n**(2) Fishery**\nThe term fishery has the meaning given the term in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ).\n**(3) Independent entity**\nThe term independent entity \u2014\n**(A)**\nmeans an entity that\u2014\n**(i)**\nis not a unit of the National Oceanic and Atmospheric Administration; and\n**(ii)**\nhas expertise in areas of science related to fishery stock assessments; and\n**(B)**\nincludes\u2014\n**(i)**\nthe National Academies of Sciences, Engineering, and Medicine; and\n**(ii)**\nan institution of higher education (as such term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )).\n**(4) MRIP**\nThe term MRIP means the Marine Recreational Information Program of the National Marine Fisheries Service.\n**(5) National Academies**\nThe term National Academies means the National Academies of Sciences, Engineering, and Medicine.\n**(6) PSE**\nThe term PSE means the percent standard error.\n**(7) Pulse species**\nThe term pulse species means a species that, due to regulatory constraints or the movement or availability of the species on a seasonal basis\u2014\n**(A)**\nis caught\u2014\n**(i)**\non an intermittent or infrequent basis; or\n**(ii)**\nonly during an abbreviated timeframe; and\n**(B)**\nis likely not sampled in a representative manner by data collected through the MRIP.\n**(8) Regional Fishery Management Council**\nThe term Regional Fishery Management Council means a Regional Fishery Management Council established under section 302 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852 ).\n**(9) Regional State fisheries commission**\nThe term regional State fisheries commission means each of\u2014\n**(A)**\nthe Atlantic States Marine Fisheries Commission;\n**(B)**\nthe Gulf States Marine Fisheries Commission; and\n**(C)**\nthe Pacific States Marine Fisheries Commission.\n**(10) Scientific and statistical committee**\nThe term scientific and statistical committee means a scientific and statistical committee established pursuant to section 302(g) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(g) ).\n**(11) Seasonal fishery**\nThe term seasonal fishery means a fishery\u2014\n**(A)**\nthat is subject to an annual closed season; or\n**(B)**\nthat may be affected by in- or post-season accountability measures that result in fishing or harvest closures.\n**(12) Standing committee**\nThe term standing committee means the standing committee established pursuant to section 3(b)(1).\n**(13) Stock of fish**\nThe term stock of fish has the meaning given the term in section 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ).\n**(14) Wave**\nThe term wave means the shortest period in which MRIP data are aggregated and reported for use in management decisions.\n#### 3. Recreational fishing data collection reform\n##### (a) In general\nThe Administrator shall reform the MRIP in effect as of the date of the enactment of this section to meet the unique needs of individual regions and States, taking into consideration the needs of State-level programs related to recreational fishing catch and effort surveys in effect as of the date of the enactment of this section to ensure that such reform does not unnecessarily dilute the effectiveness of such programs.\n##### (b) National Academies\n**(1) Standing committee**\n**(A) In general**\nThe Administrator shall enter into an agreement with the National Academies to establish a standing committee within the National Academies that shall meet regularly to discuss issues related to recreational fisheries data collection and management.\n**(B) Independence**\nIn carrying out this subsection, the standing committee shall operate independently and without the influence of the Administrator.\n**(C) Composition**\nThe standing committee shall include individuals who are experts in recreational fisheries data collection and management, including representatives from State fish and wildlife agencies.\n**(2) Consultation regarding PSE**\n**(A) In general**\nIf the PSE for data collected through the MRIP for a given seasonal fishery reaches or exceeds 30 percent in a given wave, or if a State submits a petition with respect to a given seasonal fishery under paragraph (4), the Administrator shall consult with the standing committee regarding options\u2014\n**(i)**\nto reduce the PSE of such seasonal fishery; or\n**(ii)**\nif reducing the PSE of such seasonal fishery is not practicable, to adjust the management of such seasonal fishery, including by using\u2014\n**(I)**\nthe management approaches described in section 302(h)(8) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(h)(8) ); or\n**(II)**\nmulti-year annual catch limits, including block average annual catch limits of up to 3 years.\n**(B) Report**\nAfter the Administrator consults with the standing committee under subparagraph (A) with respect to a seasonal fishery described in that subparagraph, the Administrator shall, not later than 6 months after the date on which either the PSE for data collected through the MRIP for such seasonal fishery exceeds 30 percent in a given wave or the Administrator receives a petition submitted by a State under paragraph (4), publish a report specifying\u2014\n**(i)**\nthe options considered under that subparagraph (A);\n**(ii)**\nthe recommendation of the Administrator regarding how\u2014\n**(I)**\nto reduce the PSE for data collected through the MRIP for such seasonal fishery; or\n**(II)**\nto adjust the management of such seasonal fishery in a manner that allows continued access and considers recommendations contained in the report submitted to Congress under section 102 of the Modernizing Recreational Fisheries Management Act of 2018 ( Public Law 115\u2013405 ); and\n**(iii)**\nthe reasoning, written in a manner easily understood by the public, for giving such recommendation.\n**(C) Regional Fishery Management Council**\nIf the Administrator publishes a report under subparagraph (B) with respect to a seasonal fishery described in subparagraph (A), the Administrator shall send such report to the relevant Regional Fishery Management Council for consideration.\n**(3) Consideration**\nIn carrying out paragraphs (1) and (2), the Administrator and the standing committee shall consider issues including the following:\n**(A)**\nWhether the data collected through the MRIP is appropriate and useful for management decisions, including options to improve data collection methods.\n**(B)**\nThe extent to which existing and potential data collection options are\u2014\n**(i)**\nburdensome to anglers; and\n**(ii)**\nan efficient or appropriate use of resources.\n**(C)**\nWhether and to what extent specific recommendations from the report published by the National Academies titled Data and Management Strategies for Recreational Fisheries with Annual Catch Limits (2021) and other relevant National Academies activities can and should be applied in light of the particular context of the fishery being considered.\n**(4) Petition to initiate consultation**\nA State may submit to the Administrator a petition for the Administrator to initiate the consultation process under paragraph (2) with respect to a given seasonal fishery if\u2014\n**(A)**\nthe PSE for data collected through the MRIP for such seasonal fishery is\u2014\n**(i)**\nsignificantly greater or less than the preceding 3-year average PSE for such seasonal fishery; or\n**(ii)**\nsubstantially greater than the PSE for data collected through State surveys for such seasonal fishery; or\n**(B)**\ndata collected through the MRIP for such seasonal fishery is unreliable because the stock of fish of such seasonal fishery is a pulse species.\n**(5) Combined reports**\nIn carrying out this subsection, the Administrator may carry out a single consultation with the standing committee under paragraph (2) with respect to 2 or more species if the Administrator and the standing committee jointly determine the underlying issues that triggered the consultation are highly similar.\n##### (c) Alternative to MRIP\nIf, after consultation with the standing committee and relevant States, the Administrator determines that it is not practicable to reduce the PSE for data collected through the MRIP for a given seasonal fishery to 30 percent or less, the Administrator, in collaboration with the standing committee and relevant States and stakeholders, may develop alternative data collection and monitoring methodologies and, subject to peer review and validation, use such alternative data collection and monitoring methodologies in place of the MRIP for such seasonal fishery.\n##### (d) Rule of construction\nNothing in this section may be construed to override the role of the scientific and statistical committees in advising the Regional Fishery Management Councils regarding recommendations developed pursuant to this section.\n#### 4. State recreational fishery catch and effort data collection\n##### (a) State recreational fishery catch and effort data collection program\n**(1) In general**\nA State may, subject to the approval of the Administrator, carry out a program within the waters of such State and Federal waters to collect recreational fishing catch and effort data for individual, or sets of, species that are federally managed.\n**(2) Requirements**\nIf a State carries out a program under paragraph (1), the head of such program shall\u2014\n**(A)**\nensure that such program complies with paragraph (3);\n**(B)**\ncollect recreational fishery catch and effort data with respect to such State;\n**(C)**\nreport such data that is necessary for Federal management to the Administrator in a manner and timeliness that complies with section 401 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1881 ); and\n**(D)**\ntake into consideration the burden of such program to the average angler such that such program is not overly burdensome to the point that substantial noncompliance would be expected.\n**(3) Data requirements**\nThe Administrator, in consultation with the regional State fisheries commissions, shall, with respect to data collected through a recreational fishery catch and effort data collection program of a State carried out under this subsection\u2014\n**(A)**\nestablish universal standards regarding the collection of such data, including ensuring that such standards\u2014\n**(i)**\nallow for flexibility in the design of such programs to account for differences in recreational fishing activity between States; and\n**(ii)**\nfacilitate the collection of comparable data between States within a region for the purposes of stock assessments and management; and\n**(B)**\nnot later than 3 years after the date on which a State first reports such data, develop and implement a plan to use such data\u2014\n**(i)**\nwithout calibration to data collected pursuant to any Federal program, including the MRIP; and\n**(ii)**\nas the baseline for the calibration of historic estimates of recreational catch in place of data collected through the MRIP.\n**(4) Use of State data**\n**(A) In Federal stock assessments and regulatory actions**\nData collected through a recreational fishery catch and effort data collection program of a State carried out under this subsection may be used in Federal stock assessments and regulatory actions.\n**(B) In place of MRIP data**\nIf a State collects data pursuant to this subsection that is collected pursuant to the MRIP, the Administrator shall use the data collected by the State in place of the data collected pursuant to the MRIP, including with respect to management decisions.\n**(C) Calibration with MRIP data**\n**(i) In general**\nAs applicable, data collected through the MRIP\u2014\n**(I)**\nshall be calibrated to data collected through a recreational fishery catch and effort data collection program of a State carried out under this subsection; and\n**(II)**\nmay only be so calibrated after the data described in subclause (I) is compared to data collected through such a program of another State.\n**(ii) Prohibition**\nData collected through a recreational fishery catch and effort data collection program of a State carried out under this subsection may not be calibrated to data collected through the MRIP.\n**(5) Subsequent funding**\nUpon approval by the Administrator of a recreational fishery catch and effort data collection program of a State under paragraph (1), funding previously allocated to such State for the collection of recreational fishery catch and effort data through the MRIP shall continue to be allocated to such State for such State to carry out such program of the State.\n##### (b) Grant program\n**(1) In general**\nNot later than 180 days after the date of the enactment of this section, the Administrator shall establish and carry out a grant program to award amounts to States to develop, with respect to each such State, a new, or improve an existing, program described in subsection (a).\n**(2) Applications**\nTo be eligible for a grant under this subsection, a State shall submit to the Administrator an application in such form, at such time, and containing such information as the Administrator determines appropriate.\n**(3) Use of funds**\nA State that is awarded a grant under this subsection shall use such award\u2014\n**(A)**\nto support the development or improvement of a program described in subsection (a) of such State;\n**(B)**\nto enhance the timeliness of reporting by such State of data collected by such State through such program; and\n**(C)**\nto increase the accuracy and precision of the data collected by such State pursuant to such program.\n**(4) Priority**\nIn awarding grants under this subsection, the Administrator shall give priority to applications\u2014\n**(A)**\nbased on the ability of the award to reduce the uncertainty of data collected through the MRIP, including with respect to\u2014\n**(i)**\neconomically or socially important species;\n**(ii)**\nspecies a fishery of which has had a fishing season substantially reduced or full annual closures proposed; and\n**(iii)**\nspecies a fishery of which is at risk of closing another fishery because the management of both fisheries are intermingled; and\n**(B)**\nthat would alter or improve an existing State program carried out under subsection (a) to meet the requirements under subsection (a)(3).\n##### (c) Report\nOn the date that is 2 years after the date of the enactment of this section, and biennially thereafter, the Administrator shall submit to the appropriate congressional committees and make publicly available a report regarding the implementation of this section that includes\u2014\n**(1)**\nthe number of States that have participated in the grant program established under subsection (b);\n**(2)**\na description of each State recreational fishery catch and effort data collection program;\n**(3)**\na description of how the Administrator incorporates data collected pursuant to each such program in fishery stock assessments, fishery management decisions, and catch monitoring; and\n**(4)**\nan analysis regarding the improvement in data precision and the accuracy of data collected pursuant to each such program compared to data collected through the MRIP.\n##### (d) Rule of construction\nNothing in this section may be construed to negate, uncertify, or otherwise undo existing State programs to collect recreational fishing catch and effort data.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator to carry out this section $15,000,000 for each of fiscal years 2026 through 2031.\n#### 5. Healthy fisheries through better science\n##### (a) Definition of stock assessment\nSection 3 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1802 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (43) through (50) as paragraphs (44) through (51), respectively;\n**(2)**\nby inserting after paragraph (42) the following:\n(43) The term stock assessment means an evaluation of the past, present, and future status of a stock of fish, including\u2014 (A) a range of life history characteristics for such stock of fish, including, to the extent practicable\u2014 (i) the geographical boundaries of such stock of fish; and (ii) information regarding age, growth, natural mortality, sexual maturity and reproduction, feeding habits, and habitat preferences of such stock of fish; and (B) fishing for the stock of fish. ; and\n**(3)**\nby redesignating the second paragraph (33) as paragraph (52).\n##### (b) Stock assessment plan\n**(1) In general**\nSection 404 of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1881c ) is amended by adding at the end the following:\n(f) Stock assessment plan (1) In general The Secretary shall develop and publish in the Federal Register, on the same schedule as required for each strategic plan required under subsection (b), a plan to conduct stock assessments for priority stocks of fish for which a fishery management plan is in effect under this Act. (2) Contents Each plan described in paragraph (1) shall\u2014 (A) for each priority stock of fish for which a stock assessment has previously been conducted\u2014 (i) establish a schedule for updating the stock assessment that is reasonable given the biology and characteristics of the stock of fish; and (ii) subject to the availability of appropriations, require completion of a new stock assessment, or an update of the most recent stock assessment\u2014 (I) every 5 years; or (II) within such other time period specified and justified by the Secretary in the plan; (B) for each priority stock of fish for which a stock assessment has not previously been conducted\u2014 (i) establish a schedule for conducting an initial stock assessment that is reasonable given the biology and characteristics of the stock; and (ii) subject to the availability of appropriations, require completion of the initial stock assessment not later than 3 years after the date on which the plan is published in the Federal Register unless another time period is specified and justified by the Secretary in the plan; and (C) (i) identify data and analysis, including both data and analysis that is and is not available at the time the plan is prepared, that would reduce the uncertainty, improve the accuracy, and increase the efficiency of future stock assessments; and (ii) with respect to data and analysis identified under clause (i), determine whether such data and analysis could be provided by fishermen, fishing communities, universities, and research institutions, to the extent that the use of such data would be consistent with the requirements in section 301(a)(2). (3) Waiver of stock assessment requirement Notwithstanding subparagraphs (A)(ii) and (B)(ii) of paragraph (2), a stock assessment is not required for a stock of fish in the plan described in paragraph (1) if the Secretary determines that such stock assessment is not necessary and justifies such determination in the Federal Register notice required by this subsection. .\n**(2) Deadline**\nNotwithstanding section 404(f)(1) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1881c(f)(1) ), as added by this section, the Secretary of Commerce shall issue the first stock assessment plan under section 404(f) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1881c(f) ), as added by this section, not later than 2 years after the date of the enactment of this section.\n#### 6. Fishery-Independent surveys by independent entities\n##### (a) In general\nThe Administrator shall establish a program to enter into contracts with independent entities on a competitive basis under which such independent entities shall conduct fishery-independent surveys designed to estimate the absolute abundance of stocks of fish included in the Fish Stock Sustainability Index on behalf of the Administrator.\n##### (b) Applications\nTo be eligible to enter into a contract under the program established under subsection (a), an independent entity shall submit to the Administrator an application in such form, at such time, and containing such information as the Administrator determines appropriate, including evidence of the following:\n**(1)**\nUse by the independent entity of modern or cutting-edge science.\n**(2)**\nThe ability of the independent entity to handle data in a reliable manner.\n##### (c) Use of data\nUpon favorable peer review, the Administrator, in consultation with the relevant scientific and statistical committees and independent entity and with consideration of the report submitted under section 7, shall incorporate data collected pursuant to a fishery-independent abundance survey conducted by an independent entity under the program established under subsection (a) in management decisions.\n##### (d) Report\nThe Administrator shall annually submit to the Committee on Natural Resources of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report regarding the findings of surveys conducted pursuant to this section and the incorporation of the results of such surveys in management decisions pursuant to subsection (c).\n#### 7. Report\nNot later than 1 year after the date of the enactment of this section, the National Academies, in consultation with the Harte Research Institute for Gulf of Mexico Studies, shall submit to the Committee on Natural Resources of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate and make publicly available a report regarding\u2014\n**(1)**\nthe incorporation of the results of the study titled Estimating the Absolute Abundance of Age-2+ Red Snapper (Lutjanus campechanus) in the U.S. Gulf of Mexico (August 16, 2021) in management decisions of the National Marine Fisheries Service; and\n**(2)**\nrecommendations regarding the incorporation of data collected pursuant to section 6 in management decisions of the National Marine Fisheries Service.\n#### 8. Transparency and public process\n##### (a) Advice\nSection 302(g)(1)(B) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(g)(1)(B) ) is amended by adding at the end the following: Each scientific and statistical committee shall develop such advice in a transparent manner and allow for public involvement in the process. .\n##### (b) Meetings\nSection 302(i)(2) of the Magnuson-Stevens Fishery Conservation and Management Act ( 16 U.S.C. 1852(i)(2) ) is amended by adding at the end the following:\n(G) Each Council shall make available on the internet website of the Council\u2014 (i) with respect to each meeting of the Council and Council coordination committee established under subsection (l) that is not closed in accordance with paragraph (3), to the extent practicable, a Webcast, live audio recording, or live broadcast of each such meeting; and (ii) with respect to each meeting of the Council and of the scientific and statistical committee established by the Council under subsection (g)(1)(A) that is not closed in accordance with paragraph (3), by not later than 30 days after the conclusion of each such meeting, an audio or video (if the meeting was held in person or by video conference) recording or a searchable audio or written transcript of each such meeting. (H) The Secretary shall maintain and make available to the public an archive of each recording and transcript made available under subparagraph (G). .",
      "versionDate": "2025-10-06",
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
            "name": "Advisory bodies",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T13:28:50Z"
          },
          {
            "name": "Fishes",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2026-01-20T16:43:31Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-01-20T16:43:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-09T22:29:48Z"
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
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5699ih.xml"
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
      "title": "Fisheries Data Modernization and Accuracy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fisheries Data Modernization and Accuracy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the National Oceanic and Atmospheric Administration to reform the Marine Recreational Information Program of the National Marine Fisheries Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:26Z"
    }
  ]
}
```
