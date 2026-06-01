# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/897?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/897
- Title: Aviation-Impacted Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 897
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-01 - Committee: Referred to the Subcommittee on Aviation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/897",
    "number": "897",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Aviation-Impacted Communities Act",
    "type": "HR",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:45:38Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "IL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MD"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr897ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 897\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Smith of Washington (for himself, Mr. Johnson of Georgia , Ms. Norton , Mr. Quigley , Mr. Neguse , Mr. Khanna , Ms. Brownley , Mr. Nadler , Ms. Chu , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Federal Aviation Administration to provide funding for noise mitigation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation-Impacted Communities Act .\n#### 2. Noise mitigation for vertical fenceline communities\nNotwithstanding any other provision of law, aviation-impacted communities that are not currently within the 65 DNL standard as measured by the Federal Aviation Administration shall be eligible for the Airport Improvement Program noise mitigation program funds and for grants under section 7, and shall also be granted status under section 5 to establish community boards to address airport noise in their communities.\n#### 3. National Academy of Sciences study, framework, and diagnostic tool\n##### (a) In general\nThe Administrator shall enter into a contract with the National Academy of Sciences to conduct a study that\u2014\n**(1)**\nsummarizes the relevant literature and studies done on aviation impacts worldwide; and\n**(2)**\nfocuses on large hub commercial airports and surrounding communities, including communities currently outside of the 65 DNL contour in\u2014\n**(A)**\nKing County, WA;\n**(B)**\nBoston;\n**(C)**\nChicago;\n**(D)**\nNew York City;\n**(E)**\nthe Northern California Metroplex;\n**(F)**\nPhoenix;\n**(G)**\nthe Southern California Metroplex;\n**(H)**\nthe District of Columbia;\n**(I)**\nAtlanta; and\n**(J)**\nany other metropolitan large hub airport identified by the Administrator.\n##### (b) Contents\nThe study described in subsection (a) shall examine\u2014\n**(1)**\nthe collection and consolidation of quantifiable, observational, experiential, anecdotal, or other data from\u2014\n**(A)**\nthe Federal Aviation Administration;\n**(B)**\nairport operators;\n**(C)**\nvalid acoustic instrumentation on the ground;\n**(D)**\ntestimonials and other evidence from community members; and\n**(E)**\norganizations in the community;\n**(2)**\nthe Day-Night Average Sound Level, using measured data or modeled data (or other noise metrics, as applicable);\n**(3)**\nany other existing or supplemental noise metrics from data collected by noise monitor stations;\n**(4)**\nemissions generated by individual and cumulative takeoffs and landings, including emissions that impact the ground level;\n**(5)**\nlateral trajectory and altitude of flight paths as demonstrated by actual and comprehensive radar flight track data in addition to published routes;\n**(6)**\nhow aviation impacts communities surrounded by multiple airports;\n**(7)**\nhow aviation impacts communities with unique geography, including communities situated at higher elevation or near large bodies of water;\n**(8)**\nany other data requested by the impacted community in order to give a comprehensive understanding of the impacts on such community, including comparative data for equity analysis;\n**(9)**\nrecommendations on actions or mitigation that can be taken to alleviate\u2014\n**(A)**\nconcerns raised during community outreach; and\n**(B)**\neffects that are determined in the study; and\n**(10)**\nany other data or information determined to be relevant by the National Academies in analyzing aviation impacts.\n##### (c) Framework and diagnostic tool\n**(1) In general**\nUsing findings from the study, the National Academy of Sciences shall provide the FAA with a framework and diagnostic tool for\u2014\n**(A)**\nconducting appropriate community assessments upon request of community boards (including as described in section 5(f));\n**(B)**\nmeasuring the impact on communities of\u2014\n**(i)**\nhigh frequency of overhead flights;\n**(ii)**\nan increase or change in flight operations due to adoption of new flight procedures;\n**(iii)**\nhigh frequency or an increase in night time aircraft noise; and\n**(iv)**\ndecreased dispersion of flight path utilization; and\n**(C)**\ndeveloping a scientifically based strategy for evaluating structures subject to increases described in subparagraph (A)(ii) that should be eligible for noise mitigation.\n**(2) Requirement**\nIn developing the framework and diagnostic tool under paragraph (1), the National Academy of Sciences shall\u2014\n**(A)**\nseek appropriate community input and feedback from community boards as well as open community meetings; and\n**(B)**\nensure, to the extent practicable, that such framework and diagnostic tool is understandable to, and useable by, the community boards and the general public.\n#### 4. Designating of communities\n##### (a) Outreach\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Administrator shall conduct outreach to State, regional, and local elected officials of aviation-impacted communities to inform them of the opportunity to be a designated community.\n**(2) Requirements**\nThe outreach described in paragraph (1) shall\u2014\n**(A)**\nbe conducted in local print and electronic media (including social media, local foreign language media, ethnic radio, newspapers, and television); and\n**(B)**\nreflect languages regularly encountered in the aviation-impacted community in any signs, materials, and multimedia resources.\n##### (b) Request\nThe State, regional, or local elected officials (or designee thereof) of an aviation-impacted community may request to be a designated community, and the Administrator shall\u2014\n**(1)**\nrecognize such community as a designated community upon request; and\n**(2)**\nacknowledge each community requesting designation on the website of the Federal Aviation Administration.\n##### (c) Portions of community\nThe State or local elected officials (or designee thereof) of a designated community, representatives, or a group of representatives chosen by a community, shall select the portions or the entirety of such community considered aviation-impacted, including designating the community as a whole should such community so choose.\n#### 5. Community boards\n##### (a) In general\nNot later than 6 months after the date on which an aviation-impacted community becomes a designated community pursuant to section 4, such designated community shall\u2014\n**(1)**\nselect a community board comprised of individuals that equally represent\u2014\n**(A)**\nState, regional, or local elected officials or city managers (or designees thereof);\n**(B)**\nlocal airport operators;\n**(C)**\nimpacted community residents; and\n**(D)**\nthe public health and environment; and\n**(2)**\nin the case where such designated community decides to maintain an existing group of primarily elected local officials that has previously been constituted for purposes of working on aviation-related issues, designate such existing group as a community board pursuant to this section, so long as\u2014\n**(A)**\naffected community members who are not airport employees or elected officials have representation on the board; and\n**(B)**\nhealth and environmental representatives are added as needed.\n##### (b) Meetings\nA community board shall meet at times and places chosen by the members of such board.\n##### (c) Purposes\nThe purpose of a community board is to provide information to airport operators and the Federal Aviation Administration concerning aviation impacts.\n##### (d) Collaboration\nThe Administrator shall\u2014\n**(1)**\ndesignate an FAA designee; and\n**(2)**\nensure that representatives of and, when appropriate and upon request of a community board, relevant experts from the Federal Aviation Administration participate in meetings of a community board.\n##### (e) Community reports\n**(1) In general**\nA community board may draft a community report detailing the community\u2019s concerns and issues related to aviation impacts.\n**(2) Contents**\nA community report may be comprised of, or include, community information, documents, or locally conducted assessments.\n##### (f) Community assessments\n**(1) In general**\nA community board may petition the Administrator to conduct a community assessment, which shall be conducted based on the framework and diagnostic tool established by the National Academy of Sciences under section 3 and the community reports described in subsection (e).\n**(2) Limitation**\nA community board may petition the Administrator to conduct not more than 1 community assessment under paragraph (1) every 3 years.\n**(3) Exception**\nNotwithstanding paragraph (2), a community board may petition the Administrator to conduct an additional community assessment during the 3-year period described in paragraph (2) if\u2014\n**(A)**\na study described in part 150 of title 14, Code of Federal Regulations, is commissioned by an airport with flight paths that affect the community represented by the community board; or\n**(B)**\nif airport operations increase substantially above of projected increases.\n##### (g) Instrumentation\nUpon request of a community board, the Administrator shall provide additional noise measurement instrumentation to measure aircraft noise.\n##### (h) Collaboration\nThe Administrator and each community board that petitions for a community assessment shall collaborate on the scope of such community assessment.\n##### (i) Regional assessment\nUpon the request and approval of not less than 2 community boards located in the same region, the FAA may conduct a regional assessment based on the framework and diagnostic tool established by the National Academy of Sciences under section 3.\n##### (j) Accessible format\nThe Administrator shall ensure the community assessment is culturally and linguistically accessible given the needs or requests of the community.\n#### 6. Action plans\n##### (a) In general\nNot later than 6 months after the date of completion of a community assessment described in section 5(f), the Administrator shall, in collaboration with community boards, devise an action plan that seeks to alleviate or address the concerns raised in such community reports or such community assessments.\n##### (b) Content\nAn action plan shall\u2014\n**(1)**\ninclude a long-term regional plan that focuses on reducing and minimizing aviation impacts for the designated community or communities, including sound insulation or other noise mitigation infrastructure, air filtration systems, and changes in flight paths or procedures; and\n**(2)**\nrequire the appropriate district office of the Federal Aviation Administration and air traffic control facility to consider the implementation of changes to flight operations, flight paths, and vertical guidance if the community assessment described in section 5(f) indicates that such changes would decrease the impacts on the designated community, including examining the population density in the communities described in such report and assessment in considering such implementation.\n##### (c) Implementation\nIn implementing the action plan, the Administrator will consider the implementation of changes to flight operations, flight paths, and vertical guidance if the community assessment described in section 5(f) indicates that such changes would decrease the impacts of flights on a designated community (or communities).\n##### (d) Statement concerning certain changes\nIf the Administrator determines that changes to operations, flight paths, and vertical guidance that a community study indicated would decrease the effects on the designated community would not be effective in decreasing community impacts, the Administrator shall explain the rationale for this determination in the action plan.\n##### (e) Appeals process\n**(1) In general**\nThe Administrator shall establish an appeals process, through which a community board may appeal the determination by the Federal Aviation Administration not to implement a change under subsection (c) to an independent panel comprised equally of independent public health experts, environmental experts, and aviation experts.\n**(2) Recommendations**\nIn carrying out paragraph (1), the Administrator shall seek recommendations from the National Academy of Sciences for panel experts described in such paragraph.\n**(3) Requirement to convene**\nAn independent panel convened pursuant to paragraph (1) shall convene not later than 6 months after the receipt of an appeal pursuant to such paragraph and shall respond to such appeal not later than 3 months after the date on which such panel convenes.\n##### (f) Dissemination\nThe panel described in subsection (e)(1) shall submit any findings for an appeal described in such subsection\u2014\n**(1)**\nto the public in a culturally and linguistically appropriate fashion given the needs or requests of the community at issue;\n**(2)**\nto the offices of the Members of Congress and Senators representing the community at issue;\n**(3)**\nto the relevant committees of the House of Representatives and the Senate; and\n**(4)**\nupon request, to appropriate State, regional, and local elected officials.\n#### 7. Mitigation funding\n##### (a) In general\nNot later than 180 days after the release of an action plan pursuant to section 3, the Administrator shall make grants for necessary noise mitigation in a designated community for\u2014\n**(1)**\nresidences;\n**(2)**\nhospitals;\n**(3)**\nnursing homes and adult or child day care centers;\n**(4)**\nschools;\n**(5)**\nplaces of worship; and\n**(6)**\nother impacted facilities indicated by a community assessment under section 5(f).\n##### (b) Standards\nUsing the framework and diagnostic tool developed by the National Academy of Sciences under section 3, the Administrator shall develop standards to determine which of the structures in designated communities described in subsection (a) are eligible for mitigation funding.\n##### (c) Mitigation defined\nIn this section, the term noise mitigation means any form of mitigation that reduces the noise burden for communities, including\u2014\n**(1)**\nsound insulation of structures;\n**(2)**\nconstruction of noise barriers or acoustic shielding to mitigate ground-level noise; and\n**(3)**\nother mitigation as indicated by a community assessment under section 5(f) or an action plan under section 6 using the diagnostic tool developed by the National Academy of Sciences under section 3.\n##### (d) Sound insulation for communities subject to high flight frequency\n**(1) In general**\nUsing the framework and diagnostic tool developed by the National Academy of Sciences under section 3, in carrying out an action plan described in section 6, the Administrator shall develop standards for determining which communities are subject to significant frequency of overhead flights, which shall be eligible for noise mitigation funding.\n**(2) Noise mitigation**\nIn carrying out an action plan described in section 6, the Administrator and airport operators shall provide grants for noise mitigation for aviation-impacted communities that are subjected to a high frequency of flight operations or from the adoption of new flight procedures (as determined by the Administrator through the use of the framework and diagnostic tool developed by the National Academy of Sciences under section 3).\n##### (e) Sound insulation for residences impacted by significant night time aircraft noise\nIn carrying out an action plan described in section 6, the Administrator and airport operators shall provide noise mitigation for a neighborhood within a 55 or higher DNL contour (or a community that has quality-assured noise measurement data that demonstrate 55 DNL impacts occurring outside the model contour of the aviation environmental design tool of the FAA) in which an airport operator or the Administrator determines, through the use of the framework and diagnostic tool developed by the National Academy of Sciences under section 3, that significant numbers of flight operations are conducted between 10:00 p.m. and 6:00 a.m.\n#### 8. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated out of the Airport and Airway Trust Fund (established under section 9502 of the Internal Revenue Code of 1986) to carry out this Act\u2014\n**(1)**\na total of $750,000,000 for fiscal years 2025 through 2034; and\n**(2)**\nsuch sums as necessary, but not to exceed 0.25 percent of the annual change in uncommitted balance of such Trust Fund in a fiscal year, for fiscal years after fiscal year 2034.\n##### (b) Use of funds\nOf any amounts appropriated for a fiscal year to carry out this Act, the Administrator shall use such funds\u2014\n**(1)**\nto make grants under section 7;\n**(2)**\nin an amount of not more than 5 percent, to support FAA expenditures required for the administration this Act; and\n**(3)**\nany amounts not expended under paragraph (1) or (2), to make grants described in section 47117(e)(1)(A) of title 49, United States Code.\n#### 9. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) Aircraft operation**\nThe term aircraft operation means a landing or take-off of an aircraft flight.\n**(3) Aviation-impacted community**\nThe term aviation-impacted community means a community that is located not greater than 1 mile from any point at which a commercial or cargo jet route is 3,000 feet or less above ground level.\n**(4) Commercial or cargo jet route**\nThe term commercial or cargo jet route means a route that is departing or arriving at a large hub or metroplex airport, as such terms are defined by the Administrator.\n**(5) Community**\nThe term community means any residential neighborhood, locality, municipality, town, or city.\n**(6) Designated community**\nThe term designated community means an aviation-impacted community that has chosen to be designated pursuant to section 4.\n**(7) FAA**\nThe term FAA means the Federal Aviation Administration.\n**(8) FAA designee**\nThe term FAA Designee means a community engagement manager or Regional Ombudsman (as described in section 180 of the FAA Reauthorization Act of 2018) that\u2014\n**(A)**\nworks with each community board;\n**(B)**\nengages in meaningful, solution-driven dialogue with the community board; and\n**(C)**\nserves as the liaison between the FAA and the community board.\n**(9) Impact**\nThe term impact means noise, air pollution emissions, or any other aviation-related impact identified by a community coming from an aircraft and that is affecting a community or its residents.\n**(10) Route**\nThe term route includes both the lateral trajectory and altitude of flight paths as demonstrated by actual and comprehensive radar flight track data in addition to published routes.",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-04T17:30:10Z"
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
          "measure-id": "id119hr897",
          "measure-number": "897",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr897v00",
            "update-date": "2025-04-21"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Aviation-Impacted Communities Act</strong></p><p>This bill increases access to noise mitigation\u00a0measures\u00a0for aviation-impacted communities.<em>\u00a0</em>Under the bill, an <em>aviation-impacted community</em> is a community that is located not more than one mile from any point at which a commercial or cargo jet route is 3,000 feet or less above ground level.</p><p>The bill expands noise mitigation program funding under the Airport Improvement Program to include aviation-impacted communities that are not currently within the 65 day-night average sound level (DNL) standard.</p><p>The Federal Aviation Administration (FAA) must conduct outreach to aviation-impacted communities to inform them of the opportunity to be a designated community. A designated community must form a community board to provide information to airport operators and the FAA concerning aviation impacts (e.g., aircraft noise).</p><p>A community board may petition the FAA to conduct a community assessment and, based on the assessment, the FAA must devise an action plan that alleviates or addresses the community\u2019s concerns.</p><p>In addition, the FAA must enter into an agreement with the National Academy of Sciences to conduct a study and provide the FAA with a framework and diagnostic tool for conducting community assessments.</p><p>The FAA must provide grants for necessary noise mitigation in a designated community for residences, hospitals, nursing homes, adult or child day care centers, schools, and places of worship. Further, the FAA and airport operators must provide (1)\u00a0noise mitigation grants for\u00a0communities subject to significant frequency of overhead flights,\u00a0and (2) noise mitigation for residences impacted by significant nighttime aircraft noise.</p>"
        },
        "title": "Aviation-Impacted Communities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr897.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation-Impacted Communities Act</strong></p><p>This bill increases access to noise mitigation\u00a0measures\u00a0for aviation-impacted communities.<em>\u00a0</em>Under the bill, an <em>aviation-impacted community</em> is a community that is located not more than one mile from any point at which a commercial or cargo jet route is 3,000 feet or less above ground level.</p><p>The bill expands noise mitigation program funding under the Airport Improvement Program to include aviation-impacted communities that are not currently within the 65 day-night average sound level (DNL) standard.</p><p>The Federal Aviation Administration (FAA) must conduct outreach to aviation-impacted communities to inform them of the opportunity to be a designated community. A designated community must form a community board to provide information to airport operators and the FAA concerning aviation impacts (e.g., aircraft noise).</p><p>A community board may petition the FAA to conduct a community assessment and, based on the assessment, the FAA must devise an action plan that alleviates or addresses the community\u2019s concerns.</p><p>In addition, the FAA must enter into an agreement with the National Academy of Sciences to conduct a study and provide the FAA with a framework and diagnostic tool for conducting community assessments.</p><p>The FAA must provide grants for necessary noise mitigation in a designated community for residences, hospitals, nursing homes, adult or child day care centers, schools, and places of worship. Further, the FAA and airport operators must provide (1)\u00a0noise mitigation grants for\u00a0communities subject to significant frequency of overhead flights,\u00a0and (2) noise mitigation for residences impacted by significant nighttime aircraft noise.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119hr897"
    },
    "title": "Aviation-Impacted Communities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Aviation-Impacted Communities Act</strong></p><p>This bill increases access to noise mitigation\u00a0measures\u00a0for aviation-impacted communities.<em>\u00a0</em>Under the bill, an <em>aviation-impacted community</em> is a community that is located not more than one mile from any point at which a commercial or cargo jet route is 3,000 feet or less above ground level.</p><p>The bill expands noise mitigation program funding under the Airport Improvement Program to include aviation-impacted communities that are not currently within the 65 day-night average sound level (DNL) standard.</p><p>The Federal Aviation Administration (FAA) must conduct outreach to aviation-impacted communities to inform them of the opportunity to be a designated community. A designated community must form a community board to provide information to airport operators and the FAA concerning aviation impacts (e.g., aircraft noise).</p><p>A community board may petition the FAA to conduct a community assessment and, based on the assessment, the FAA must devise an action plan that alleviates or addresses the community\u2019s concerns.</p><p>In addition, the FAA must enter into an agreement with the National Academy of Sciences to conduct a study and provide the FAA with a framework and diagnostic tool for conducting community assessments.</p><p>The FAA must provide grants for necessary noise mitigation in a designated community for residences, hospitals, nursing homes, adult or child day care centers, schools, and places of worship. Further, the FAA and airport operators must provide (1)\u00a0noise mitigation grants for\u00a0communities subject to significant frequency of overhead flights,\u00a0and (2) noise mitigation for residences impacted by significant nighttime aircraft noise.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119hr897"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr897ih.xml"
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
      "title": "Aviation-Impacted Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation-Impacted Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Aviation Administration to provide funding for noise mitigation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:32Z"
    }
  ]
}
```
