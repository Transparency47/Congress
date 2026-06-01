# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6041?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6041
- Title: Rural Partnership and Prosperity Act
- Congress: 119
- Bill type: HR
- Bill number: 6041
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-05-16T08:07:13Z
- Update date including text: 2026-05-16T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-12-05 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6041",
    "number": "6041",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Rural Partnership and Prosperity Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:13Z",
    "updateDateIncludingText": "2026-05-16T08:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-05T19:48:08Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MD"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6041ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6041\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Ms. Salinas (for herself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo authorize the Secretary of Agriculture to provide rural partnership program grants and rural partnership technical assistance grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Partnership and Prosperity Act .\n#### 2. Definitions\nIn this Act:\n**(1) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(2) Rural; rural area**\nThe terms rural and rural area have the meaning given those terms in section 343(a)(13)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a)(13)(A) ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n#### 3. Rural partnership program grants\n##### (a) In general\nSubject to the availability of appropriations under subsection (j), the Secretary shall establish a program to make multiyear grant awards to coordinate Federal, nonprofit, and for-profit investment in rural areas.\n##### (b) Grant requirements\n**(1) Term**\nThe term of a grant awarded under subsection (a) shall be not less than 2 years and not more than 5 years.\n**(2) Awards**\nExcept as provided in paragraphs (3) and (4), the State offices of the rural development mission area shall be responsible for reviewing applications for grant awards under subsection (a) and selecting eligible applicants described in subsection (d) for those grant awards.\n**(3) Tribal awards**\nExcept as provided in paragraph (4), in the case of grants under subsection (a) allocated to Indian Tribes under subsection (c)(1)(B), the national office of the rural development mission area shall be responsible for reviewing applications for grant awards under subsection (a) and selecting eligible applicants described in subsection (d) for those grant awards.\n**(4) Competitive process**\nIf the amount appropriated under subsection (j) for a fiscal year is less than or equal to $300,000,000, the national office of the rural development mission area shall be responsible for reviewing applications for grant awards under subsection (a) and selecting eligible applicants described in subsection (d) for those grant awards\u2014\n**(A)**\non a competitive basis; and\n**(B)**\nby giving priority to areas that have higher nonmetropolitan poverty levels and lower population levels, while ensuring that grants under this section are awarded in diverse geographic regions of the United States.\n##### (c) Grant allocation\n**(1) In general**\nExcept as provided in subsection (b)(4), the Secretary shall allocate funding for grants under subsection (a)\u2014\n**(A)**\nfor each State based on a formula determined by the Secretary in accordance with paragraph (2); and\n**(B)**\nfor Indian Tribes in such amounts as the Secretary determines to be appropriate, subject to the condition that the total amount allocated to Indian Tribes under this subparagraph shall not be less than 5 percent of the amount appropriated under subsection (j), with Indian Tribes located in areas that have higher poverty levels and lower populations receiving higher levels of funding.\n**(2) Allocation requirements**\n**(A) In general**\nThe Secretary shall develop a graduated scale to allocate funding for States under paragraph (1)(A) based on the nonmetropolitan poverty and population levels in each State.\n**(B) Limitation**\nThe amount allocated to any State under subparagraph (A) shall not exceed 5 percent of the amount appropriated under subsection (j).\n**(3) Small State exception to formula**\nNotwithstanding paragraphs (1)(A) and (2)(A), the Secretary shall ensure that each State is allocated an amount for grants under this subsection that is sufficient to fulfill the purposes of the program established under this section, as determined by the Secretary.\n**(4) Reallocation**\nIf a State or Indian Tribe does not use funds allocated to the State or Indian Tribe under this subsection, the Secretary may reallocate the unused funds to 1 or more other States or Indian Tribes, each of which has used all of the funding allocated to the State or Indian Tribe under this subsection.\n##### (d) Eligible applicants\nTo be eligible to receive a grant under subsection (a), an applicant shall\u2014\n**(1)**\npropose to serve a rural area;\n**(2)**\nbe composed of a partnership of 2 or more of\u2014\n**(A)**\nan instrumentality or political subdivision of a State, such as a municipality, county, district, or authority;\n**(B)**\na nonprofit corporation or association with significant ties to the rural area described in paragraph (1), including through\u2014\n**(i)**\nassociation with, or control by, 1 or more public bodies in the rural area;\n**(ii)**\nbroadly based ownership and control by members of the rural area; or\n**(iii)**\na substantial public funding contribution to the rural area through taxes, revenue bonds, other local government sources, or substantial voluntary community funding;\n**(C)**\na cooperative with significant ties to the rural area described in paragraph (1);\n**(D)**\na for-profit entity with a significant presence in the rural area described in paragraph (1);\n**(E)**\nan institution of higher education\u2014\n**(i)**\nwith a significant contribution to or presence in the rural area described in paragraph (1); and\n**(ii)**\nthat includes representatives who are members of the rural area; and\n**(F)**\nan Indian Tribe\u2014\n**(i)**\nin a rural area described in paragraph (1); and\n**(ii)**\nwith demonstrated support from the Tribal council or duly elected Tribal executive of the appropriate Tribal government; and\n**(3)**\ndemonstrate cooperation among the members of the partnership described in paragraph (2) necessary to complete comprehensive, asset-based rural development through eligible activities described in subsection (e).\n##### (e) Eligible activities\nAn eligible applicant described in subsection (d) that receives a grant under subsection (a) may use the grant funds in rural areas\u2014\n**(1)**\nto coordinate Federal, State, regional, or Tribal initiatives to reduce duplicative efforts with respect to Federal investments;\n**(2)**\nto leverage non-Federal financial and technical resources;\n**(3)**\nto complete comprehensive predevelopment activities and planning;\n**(4)**\nto create public-private partnerships and attract private investment;\n**(5)**\nto support eligible operational activities, including staffing, of the eligible applicants, except that a for-profit entity may not use the grant funds for the purpose described in this paragraph;\n**(6)**\nto provide capital to existing or new projects, subject to the condition that not more than 50 percent of the grant funds may be used for that purpose;\n**(7)**\nto support regional projects and initiatives;\n**(8)**\nto address economic recovery from emergencies and natural or man-made disasters; and\n**(9)**\nto develop strategic community investment plans described in section 379H(d) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008v(d) ).\n##### (f) Ineligible activities\nAn eligible applicant described in subsection (d) that receives a grant under subsection (a) may not use the grant funds\u2014\n**(1)**\nto fund operational activities, including staffing, at a for-profit institution;\n**(2)**\nto purchase or lease real property; or\n**(3)**\nto support a non-rural area.\n##### (g) Selection criteria\nIn awarding grants under subsection (b), the Secretary shall give priority to an eligible applicant described in subsection (d) that proposes to serve\u2014\n**(1)**\na rural area with a significant change in population;\n**(2)**\na rural area with significant workforce changes or changes in major employers;\n**(3)**\nan economically distressed rural area, as determined by the Secretary;\n**(4)**\na rural area that has historically received minimal Federal funding, as determined by the Secretary; or\n**(5)**\na rural area for the purpose of job retention and economic stabilization, as determined by the Secretary.\n##### (h) Matching funds\n**(1) In general**\nSubject to paragraph (2), an eligible applicant described in subsection (d) that receives a grant under subsection (a) shall provide non-Federal matching funds in the form of cash or an in-kind contribution in an amount that is not less than 25 percent of the amount of the grant.\n**(2) Waiver**\n**(A) In general**\nThe Secretary may waive the requirement under paragraph (1) based on the demonstrated need of the eligible applicant or the population served by the eligible applicant, as determined by the Secretary, including\u2014\n**(i)**\nan eligible applicant serving an area with a higher nonmetropolitan poverty level;\n**(ii)**\nan eligible applicant serving a Tribal population; and\n**(iii)**\nan eligible applicant composed of a partnership that includes an entity described in subsection (d)(2)(A).\n**(B) Justification**\nThe Secretary shall provide to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a justification for each waiver provided under subparagraph (A).\n**(3) Providers**\nNon-Federal matching funds under paragraph (1) may be provided by any member of the applicable partnership described in subsection (d)(2).\n##### (i) Coordination\nThe Secretary shall carry out this section in coordination with the Rural Partners Network established by section 6306 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2204b\u20133 ).\n##### (j) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary such sums as are necessary to carry out this section.\n**(2) Administration**\nThe Secretary may retain not more than 2 percent of the amounts made available to carry out this section for administration of the program established under this section.\n#### 4. Rural partnership technical assistance grants\n##### (a) In general\nSubject to the availability of appropriations under subsection (g), the Secretary shall establish a program to award grants, on a competitive basis, for up to a 5-year period, to be administered at the national level through the Under Secretary for Rural Development, for the purpose of advising on and assisting rural community organizations with\u2014\n**(1)**\nFederal grant management and the development of financial management systems;\n**(2)**\nhousing or community economic development projects; and\n**(3)**\nthe development of placemaking plans and applications for Federal grants.\n##### (b) Eligible applicants\nTo be eligible to receive a grant under subsection (a), an applicant shall be a qualified private or nonprofit intermediary organization, including an institution of higher education with an existing community development and planning program, including an extension program, that has demonstrated experience and capacity to provide technical assistance on community development and planning in rural areas.\n##### (c) Eligible activities\nAn eligible applicant described in subsection (b) that receives a grant under subsection (a) may use the grant funds to support the capacity building and economic development of identified rural areas and local partners in those rural areas through the following activities:\n**(1)**\nTraining and supporting local staff, including relating to systems development and support.\n**(2)**\nIdentifying vetted technical consultants for planning and designing physical infrastructure.\n**(3)**\nFacilitating coordination between Federal agencies and local partners.\n**(4)**\nProviding expertise on developing public-private partnerships.\n**(5)**\nDevelopment and project predevelopment activities.\n**(6)**\nGrant writing and grant management activities.\n##### (d) Ineligible activities\nAn eligible applicant described in subsection (b) that receives a grant under subsection (a) may not use the grant funds\u2014\n**(1)**\nto fund staffing at a for-profit entity;\n**(2)**\nto purchase or lease real property, buildings, or equipment;\n**(3)**\nto support a non-rural area; or\n**(4)**\nfor research and development.\n##### (e) Priority\nIn awarding grants under subsection (a), the Secretary may give priority to an eligible applicant described in subsection (b) that serves\u2014\n**(1)**\na nonmetropolitan area with a high poverty level; or\n**(2)**\nan Indian Tribe with demonstrated support from the Tribal council or duly elected Tribal executive of the appropriate Tribal government.\n##### (f) Matching funds\n**(1) In general**\nSubject to paragraph (2), an eligible applicant described in subsection (b) that receives a grant under subsection (a) shall provide non-Federal matching funds in an amount that is not less than 30 percent of the amount of the grant.\n**(2) Waiver**\n**(A) In general**\nThe Secretary may waive the requirement under paragraph (1) based on the demonstrated need of the area in which activities using the grant are to be carried out, as determined by the Secretary.\n**(B) Justification**\nThe Secretary shall provide to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a justification for each waiver provided under subparagraph (A).\n##### (g) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary such sums as are necessary to carry out this section.\n**(2) Administration**\nThe Secretary may retain not more than 2 percent of the amounts made available to carry out this section for administration of the program established under this section.\n#### 5. Rural Partners Network\nSection 6306 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2204b\u20133 ) is amended\u2014\n**(1)**\nin the section heading, by striking Council on rural community innovation and economic development and inserting Rural Partners Network ;\n**(2)**\nin subsection (a)(1), by striking council and inserting network ;\n**(3)**\nby striking subsection (b) and inserting the following:\n(b) Establishment (1) In general There is established a Rural Partners Network (referred to in this section as the Network ). (2) Successor The Network shall be the successor to the Council on Rural Community Innovation and Economic Development established by this section (as in effect on the day before the date of enactment of the Rural Partnership and Prosperity Act ). ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking subparagraphs (C), (D), (N), (Q), (R), (S), (T), (V), (X), (Y), and (Z);\n**(ii)**\nby redesignating subparagraphs (E) through (M), (O), (P), (U), (W), and (AA) as subparagraphs (C) through (K), (L), (M), (N), (O), and (X), respectively; and\n**(iii)**\nby inserting after subparagraph (O) (as so redesignated) the following:\n(P) The Federal Deposit Insurance Corporation. (Q) The Appalachian Regional Commission. (R) The Consumer Financial Protection Bureau. (S) The Social Security Administration. (T) The Delta Regional Authority. (U) The Denali Commission. (V) The Northern Border Regional Commission. (W) The Southeast Crescent Regional Commission. ; and\n**(B)**\nin paragraphs (2) through (4), by striking Council each place it appears and inserting Network ;\n**(5)**\nin subsection (d), by striking Council and inserting Network ;\n**(6)**\nin subsection (e)\u2014\n**(A)**\nin the subsection heading, by striking Council and inserting Network ;\n**(B)**\nin the matter preceding paragraph (1), by striking Council and inserting Network ;\n**(C)**\nin paragraph (2), by striking and at the end;\n**(D)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(E)**\nby adding at the end the following:\n(4) to improve the efficiency of Federal assistance to rural communities by\u2014 (A) reducing administrative burdens on rural communities to pursue Federal funding; (B) improving the administrative efficiency of Federal economic development programs serving rural communities; and (C) streamlining and simplifying the application process for Federal funding opportunities for rural communities. ;\n**(7)**\nin subsection (f), in the matter preceding paragraph (1), by striking Council and inserting Network ;\n**(8)**\nin subsection (g), by striking Council each place it appears and inserting Network ; and\n**(9)**\nby striking subsection (h) and inserting the following:\n(h) Innovative cross-Agency coordination (1) In general The Secretary, acting as Chair of the Network, may carry out innovative strategies for coordinating with other Federal departments and agencies with respect to programs that serve rural areas. (2) Priorities In carrying out paragraph (1), the Secretary shall prioritize\u2014 (A) improving ease of access to Federal programs for resource-constrained rural communities; (B) utilizing early technical assistance to reduce duplicative applications and administrative costs at the Federal level; (C) leveraging partnerships with local, State, philanthropic, and private entities to maximize returns on Federal investments; (D) integrating stakeholder and program user experience into program design; and (E) targeting areas experiencing economic distress, as determined by the Secretary. .",
      "versionDate": "2025-11-12",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T18:21:43Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6041ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Partnership and Prosperity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T05:23:16Z"
    },
    {
      "title": "Rural Partnership and Prosperity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Agriculture to provide rural partnership program grants and rural partnership technical assistance grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T05:18:15Z"
    }
  ]
}
```
