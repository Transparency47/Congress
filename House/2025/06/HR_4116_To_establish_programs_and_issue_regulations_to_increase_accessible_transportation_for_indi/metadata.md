# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4116
- Title: Disability Access to Transportation Act
- Congress: 119
- Bill type: HR
- Bill number: 4116
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-02-04T04:11:36Z
- Update date including text: 2026-02-04T04:11:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-25 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-25 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4116",
    "number": "4116",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Disability Access to Transportation Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:36Z",
    "updateDateIncludingText": "2026-02-04T04:11:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-25T20:56:26Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4116ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4116\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Ms. Titus (for herself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo establish programs and issue regulations to increase accessible transportation for individuals with disabilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Disability Access to Transportation Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the Centers for Disease Control and Prevention, 1 in 4 U.S. adults has a disability.\n**(2)**\nSection 2(b) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 ) recognized that individuals with disabilities face discrimination when using transportation services and sought to provide a clear and comprehensive national mandate for the elimination of discrimination against individuals with disabilities .\n**(3)**\nThirty-five years after the enactment of the Americans with Disabilities Act, individuals with disabilities continue to face systemic discrimination and a lack of accessible transportation options.\n**(4)**\nTransportation is a core component of independent living; without the ability to easily move from one location to another, especially to drop a child off at day care, arrive at work on time, or run basic errands, true community living is impossible.\n**(5)**\nTechnology is changing the way the transportation industry provides services.\n**(6)**\nParatransit services often use outdated methods for dispatch and routing. Paratransit riders are not able to track the status of their rides and are often given 30 minute or longer pick-up windows before or after the rider\u2019s desired departure time. Lengthy pick-up windows result in uncertainty about driver arrival times.\n**(7)**\nThe majority of paratransit services do not allow riders to book day-of services. In such cases, riders are required to book trips at least 1 day prior. Without a same-day service solution, riders have no way to address urgent healthcare, employment or other needs that arise. Adding this capability to paratransit services would be hugely impactful to riders.\n**(8)**\nAs technology continues to change the way people move from one place to another, the transportation sector, including Federal agencies, local transit systems, and private entities must innovate and provide services in a way that increases access to these services and empowers individuals with disabilities to travel independently in their communities.\n#### 3. One-stop paratransit pilot program\n##### (a) In general\nNot later than 6 months after the date of enactment of this Act, the Secretary of Transportation shall establish a one-stop paratransit pilot program.\n##### (b) Purpose\nThe purpose of the pilot program under this section is to develop or expand paratransit programs carried out pursuant to the ADA to provide for at least 1 stop of at least 15 minutes outside of the vehicle during a paratransit trip to prevent long wait times between multiple trips that unduly limit an individual\u2019s ability to complete essential tasks.\n##### (c) Eligible entities\n**(1) In general**\nAn entity eligible to participate in the pilot program is a transit agency that agrees to use the existing operator of the paratransit service and its workforce, such workforce to be directly employed by the eligible entity or its contractor, to implement the pilot program and to track and share information as the Secretary requires, including\u2014\n**(A)**\nnumber of ADA paratransit trips conducted each year;\n**(B)**\nrequested time of each paratransit trip;\n**(C)**\nscheduled time of each paratransit trip;\n**(D)**\nactual pickup time for each paratransit trip;\n**(E)**\naverage length of a stop in the middle of a ride as allowed by this section;\n**(F)**\nany complaints received from a paratransit rider;\n**(G)**\nrider satisfaction with paratransit services; and\n**(H)**\nafter the completion of the pilot program, an assessment by the eligible entity of its capacity to continue a one-stop program independently.\n**(2) Preference**\nThe Secretary shall give preference to entities that\u2014\n**(A)**\nhave comparable data for the year prior to implementation of the pilot program that can be used by the Secretary and other organizations, such as nonprofit organizations and advocacy organizations, for research purposes;\n**(B)**\nplan to use the existing operator of the paratransit service and its workforce, such workforce to be directly employed by the eligible entity or its contractor, to implement the pilot program; and\n**(C)**\nplan to use technology innovation to improve the rider experience and cost-effectiveness of ADA paratransit services, including\u2014\n**(i)**\ndynamic routing;\n**(ii)**\nreal-time tracking; and\n**(iii)**\nscheduling same-day rides with on-demand capabilities.\n##### (d) Application\nTo be eligible to participate in the pilot program, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including information on\u2014\n**(1)**\nmethodology for informing the public of the pilot program;\n**(2)**\nvehicles, personnel, and other resources that will be used to implement the pilot program; and\n**(3)**\nif the applicant does not intend the pilot program to apply to the full area under the jurisdiction of the applicant, a required description of the geographic area in which the applicant intends the pilot program to apply.\n##### (e) Selection\nThe Secretary shall seek to achieve diversity of participants in the pilot program by selecting a range of eligible entities that includes at least 5 of each of the following:\n**(1)**\nAn eligible entity that serves an area with a population of 200,000 people or fewer.\n**(2)**\nAn eligible entity that serves an area with a population of over 200,000 people.\n**(3)**\nAn eligible entity that provides transportation for rural communities.\n##### (f) Report\nNot later than 6 months after the conclusion of the first 15 pilot projects carried out under this section, the Secretary shall submit to Congress a report on the results of the program, including the feasibility of developing and implementing one-stop programs for all ADA paratransit services.\n##### (g) Funding\n**(1) Federal share**\nThe Federal share of the total cost of a project carried out under this section may not exceed 80 percent.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated to carry out this section $75,000,000 for each of fiscal years 2025 through 2029.\n#### 4. Pedestrian facilities in the public right-of-way\nNot later than 180 days after the date of enactment of this Act, the Attorney General shall issue such regulations as are necessary to adopt enforceable standards for new construction and alterations of pedestrian facilities in the public right-of-way that comply with the guidance issued by the Architectural and Transportation Barriers Compliance Board, pursuant to section 502(b)(3) of the Rehabilitation Act of 1973 ( 29 U.S.C. 792(b)(3) ), under part 1190 of title 36, Code of Federal Regulations.\n#### 5. Reporting accessibility complaints\n##### (a) In general\nThe Secretary of Transportation shall ensure that an individual who believes that he or she or a specific class of individuals has been subjected to discrimination on the basis of disability by a public entity may, by himself or herself or by an authorized representative, easily file a complaint with the Department of Transportation.\n##### (b) Procedures\nNot later than 1 year after the date of enactment of this Act, the Secretary shall implement procedures that allow an individual to submit a complaint described in subsection (a) by phone, by mail-in form, and online through the website of the Office of Civil Rights of the Federal Transit Administration.\n##### (c) Notice to individuals with disabilities\nNot later than 18 months after the date of enactment of this Act, the Secretary shall require that each public transit provider and contractor providing paratransit services shall include on a publicly available website of the service provider, any related mobile device application, and online service\u2014\n**(1)**\nthe telephone number, or a comparable electronic means of communication, for the disability assistance hotline of the Office of Civil Rights of the Federal Transit Administration;\n**(2)**\nnotice that a consumer can file a disability-related complaint with the Office of Civil Rights of the Federal Transit Administration;\n**(3)**\nan active link to the website of the Office of Civil Rights of the Federal Transit Administration for an individual to file a disability-related complaint; and\n**(4)**\nnotice that an individual can file a disability-related complaint with the local transit agency and the process and any timelines for filing such a complaint.\n##### (d) Investigation of complaints\nNot later than 60 days after the last day of each fiscal year the Secretary shall publish a report that lists the disposition of complaints described in subsection (a), including\u2014\n**(1)**\nthe number and type of complaints filed with Department of Transportation;\n**(2)**\nthe number of complaints investigated by the Department;\n**(3)**\nthe result of the complaints that were investigated by the Department including whether the complaint was resolved\u2014\n**(A)**\ninformally;\n**(B)**\nby issuing a violation through a noncompliance Letter of Findings; or\n**(C)**\nby other means, which shall be described in detail; and\n**(4)**\nif a violation was issued for a complaint, whether the Department resolved the noncompliance by\u2014\n**(A)**\nreaching a voluntary compliance agreement with the entity;\n**(B)**\nreferring the matter to the Attorney General; or\n**(C)**\nby other means, which shall be described in detail.\n##### (e) Report\nUpon implementation of this section, the Secretary shall, to the extent practicable, issue a report composed of the information collected under this section for the preceding 5 years.\n#### 6. Accessibility data pilot program\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish an accessibility data pilot program.\n##### (b) Purpose\nIn carrying out the pilot program, the Secretary shall develop or procure an accessibility data set and make that data set available to each eligible entity selected to participate in the pilot program to improve the transportation planning of such eligible entities by\u2014\n**(1)**\nmeasuring the level of access by multiple transportation modes, including transportation network companies, to desired destinations, which may include connections between modes, including connections to\u2014\n**(A)**\nhigh-quality transit or rail service;\n**(B)**\nsafe bicycling corridors; and\n**(C)**\nsafe sidewalks that achieve compliance with applicable requirements of the ADA;\n**(2)**\ndisaggregating the level of access by multiple transportation modes by a variety of population categories, which shall include\u2014\n**(A)**\nlow-income populations;\n**(B)**\nminority populations;\n**(C)**\nage;\n**(D)**\ndisability such as sensory, cognitive, and physical, including wheelchair users; and\n**(E)**\ngeographical location; and\n**(3)**\nassessing the change in accessibility that would result from new transportation investments.\n##### (c) Eligible entities\nAn entity eligible to participate in the pilot program is\u2014\n**(1)**\na State;\n**(2)**\na metropolitan planning organization; or\n**(3)**\na rural transportation planning organization.\n##### (d) Application\nTo be eligible to participate in the pilot program, an entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including information relating to\u2014\n**(1)**\nprevious experience of the eligible entity measuring transportation access or other performance management experience;\n**(2)**\nthe types of important destinations to which the eligible entity intends to measure access;\n**(3)**\nthe types of data disaggregation the eligible entity intends to pursue;\n**(4)**\na general description of the methodology the eligible entity intends to apply; and\n**(5)**\nif the applicant does not intend the pilot program to apply to the full area under the jurisdiction of the applicant, a description of the geographic area in which the applicant intends the pilot program to apply.\n##### (e) Selection\n**(1) In general**\nThe Secretary shall seek to achieve diversity of participants in the pilot program by selecting a range of eligible entities that shall include\u2014\n**(A)**\nStates;\n**(B)**\nmetropolitan planning organizations that serve an area with a population of 200,000 people or fewer;\n**(C)**\nmetropolitan planning organizations that serve an area with a population of over 200,000 people; and\n**(D)**\nrural transportation planning organizations.\n**(2) Inclusions**\nThe Secretary shall seek to ensure that, among the eligible entities selected under paragraph (1) program participants represent\u2014\n**(A)**\na range of capacity and previous experience with measuring transportation access; and\n**(B)**\na variety of proposed methodologies and focus areas for measuring level of access.\n##### (f) Duties\nFor each eligible entity participating in the pilot program, the Secretary shall\u2014\n**(1)**\ndevelop or acquire an accessibility data set described in subsection (b); and\n**(2)**\nsubmit the data set to the eligible entity.\n##### (g) Methodology\nIn calculating the measures for the data set under the pilot program, the Secretary shall ensure that methodology is open source.\n##### (h) Availability\nThe Secretary shall make an accessibility data set under the pilot program available to\u2014\n**(1)**\nunits of local government within the jurisdiction of the eligible entity participating in the pilot program; and\n**(2)**\nresearchers.\n##### (i) Report\nNot later than 120 days after the last date on which the Secretary submits data sets to the eligible entity under subsection (f), the Secretary shall submit to Congress a report on the results of the program, including the feasibility of developing and providing periodic accessibility data sets for all States, regions, and localities.\n##### (j) Funding\nThe Secretary shall carry out the pilot program using amounts made available to the Secretary for administrative expenses to carry out programs under the authority of the Secretary.\n##### (k) Sunset\nThe pilot program shall terminate on the date that is 8 years after the date on which the pilot program is implemented.\n#### 7. Definitions\nIn this Act:\n**(1) ADA**\nThe term ADA means the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n**(2) State**\nThe term State means each of the several States, the District of Columbia, and any commonwealth, territory, or possession of the United States.\n**(3) Transportation network company**\nThe term transportation network company \u2014\n**(A)**\nmeans a corporation, partnership, sole proprietorship, or other entity, that uses an online-enabled application or digital network to connect riders to drivers affiliated with the entity in order for the driver to transport the rider using a vehicle owned, leased, or otherwise authorized for use by the driver to a point chosen by the rider; and\n**(B)**\ndoes not include a shared-expense carpool or vanpool arrangement that is not intended to generate profit for the driver.",
      "versionDate": "2025-06-24",
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
        "updateDate": "2025-07-17T11:12:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-24",
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
          "measure-id": "id119hr4116",
          "measure-number": "4116",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-24",
          "originChamber": "HOUSE",
          "update-date": "2026-01-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4116v00",
            "update-date": "2026-01-05"
          },
          "action-date": "2025-06-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disability Access to Transportation Act</strong></p><p>This bill establishes programs and requirements to expand transportation access for individuals with disabilities.</p><p>The Department of Transportation (DOT) must establish a one-stop paratransit pilot program. (Paratransit is often a service for the elderly and disabled using small buses and vans.) This program must develop or expand transit agency paratransit programs carried out pursuant to the Americans with Disabilities Act of 1990 (ADA) to prevent long wait times between multiple trips that unduly limit an individual's ability to complete essential tasks.</p><p>For new construction and alterations of pedestrian facilities in the public right-of-way (e.g., shared use paths),\u00a0the Department of Justice must adopt enforceable standards that comply with guidance issued by the Architectural and Transportation Barriers Compliance Board (i.e., the\u00a0Access Board), an independent federal agency.</p><p>In addition, DOT must implement procedures that allow an individual who believes that they have been subjected to discrimination on the basis of a disability by a public entity to submit an ADA complaint by phone, by mail-in form, and online. DOT must require each public transit provider and contractor providing paratransit services to post certain information on how an individual can file a disability-related complaint. In addition, DOT must publish yearly reports on the disposition of these accessibility complaints.</p><p>Finally, DOT must create an accessibility data pilot program to provide data sets to states and metropolitan or rural planning organizations to\u00a0improve their transportation planning.\u00a0</p>"
        },
        "title": "Disability Access to Transportation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4116.xml",
    "summary": {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disability Access to Transportation Act</strong></p><p>This bill establishes programs and requirements to expand transportation access for individuals with disabilities.</p><p>The Department of Transportation (DOT) must establish a one-stop paratransit pilot program. (Paratransit is often a service for the elderly and disabled using small buses and vans.) This program must develop or expand transit agency paratransit programs carried out pursuant to the Americans with Disabilities Act of 1990 (ADA) to prevent long wait times between multiple trips that unduly limit an individual's ability to complete essential tasks.</p><p>For new construction and alterations of pedestrian facilities in the public right-of-way (e.g., shared use paths),\u00a0the Department of Justice must adopt enforceable standards that comply with guidance issued by the Architectural and Transportation Barriers Compliance Board (i.e., the\u00a0Access Board), an independent federal agency.</p><p>In addition, DOT must implement procedures that allow an individual who believes that they have been subjected to discrimination on the basis of a disability by a public entity to submit an ADA complaint by phone, by mail-in form, and online. DOT must require each public transit provider and contractor providing paratransit services to post certain information on how an individual can file a disability-related complaint. In addition, DOT must publish yearly reports on the disposition of these accessibility complaints.</p><p>Finally, DOT must create an accessibility data pilot program to provide data sets to states and metropolitan or rural planning organizations to\u00a0improve their transportation planning.\u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr4116"
    },
    "title": "Disability Access to Transportation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disability Access to Transportation Act</strong></p><p>This bill establishes programs and requirements to expand transportation access for individuals with disabilities.</p><p>The Department of Transportation (DOT) must establish a one-stop paratransit pilot program. (Paratransit is often a service for the elderly and disabled using small buses and vans.) This program must develop or expand transit agency paratransit programs carried out pursuant to the Americans with Disabilities Act of 1990 (ADA) to prevent long wait times between multiple trips that unduly limit an individual's ability to complete essential tasks.</p><p>For new construction and alterations of pedestrian facilities in the public right-of-way (e.g., shared use paths),\u00a0the Department of Justice must adopt enforceable standards that comply with guidance issued by the Architectural and Transportation Barriers Compliance Board (i.e., the\u00a0Access Board), an independent federal agency.</p><p>In addition, DOT must implement procedures that allow an individual who believes that they have been subjected to discrimination on the basis of a disability by a public entity to submit an ADA complaint by phone, by mail-in form, and online. DOT must require each public transit provider and contractor providing paratransit services to post certain information on how an individual can file a disability-related complaint. In addition, DOT must publish yearly reports on the disposition of these accessibility complaints.</p><p>Finally, DOT must create an accessibility data pilot program to provide data sets to states and metropolitan or rural planning organizations to\u00a0improve their transportation planning.\u00a0</p>",
      "updateDate": "2026-01-05",
      "versionCode": "id119hr4116"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4116ih.xml"
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
      "title": "Disability Access to Transportation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disability Access to Transportation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish programs and issue regulations to increase accessible transportation for individuals with disabilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:18:24Z"
    }
  ]
}
```
