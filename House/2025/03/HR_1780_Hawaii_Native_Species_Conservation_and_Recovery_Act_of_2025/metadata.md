# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1780
- Title: Hawaii Native Species Conservation and Recovery Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1780
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-01-21T06:49:33Z
- Update date including text: 2026-01-21T06:49:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-03-03 - IntroReferral: Sponsor introductory remarks on measure. (CR E176-177)
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-03-03 - IntroReferral: Sponsor introductory remarks on measure. (CR E176-177)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1780",
    "number": "1780",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Hawaii Native Species Conservation and Recovery Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-21T06:49:33Z",
    "updateDateIncludingText": "2026-01-21T06:49:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E176-177)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:04:30Z",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1780ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1780\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Case (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish a competitive grant program to support the conservation and recovery of native plant, fungi, and animal species in the State of Hawaii, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hawaii Native Species Conservation and Recovery Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\nthe State;\n**(B)**\na unit of local government in the State;\n**(C)**\na Native Hawaiian organization;\n**(D)**\na nonprofit organization;\n**(E)**\na business; and\n**(F)**\nan institution of higher education.\n**(2) Grant program**\nThe term grant program means the Hawaii Native Species Conservation and Recovery Grant Program established under section 3(a).\n**(3) Native Hawaiian organization**\nThe term Native Hawaiian organization has the meaning given the term in section 3 of the NATIVE Act ( 25 U.S.C. 4352 ).\n**(4) Native species**\nThe term native species means a plant, fungi, or animal species that is native to the State.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(6) State**\nThe term State means the State of Hawaii.\n#### 3. Hawaii Native Species Conservation and Recovery Grant Program\n##### (a) Establishment\nNot later than 180 days after the date on which amounts are appropriated to carry out this Act, the Secretary shall establish a grant program, to be known as the Hawaii Native Species Conservation and Recovery Grant Program , to annually provide, through cooperative agreements, grants, micro grants, or other means, funding to eligible entities to carry out projects that\u2014\n**(1)**\nachieve the funding priorities developed under subsection (c); and\n**(2)**\nmeet the criteria developed under subsection (e).\n##### (b) Purpose\nThe grant program shall identify priorities and provide funding and technical assistance to carry out coordinated, evidence-based conservation and recovery projects in the State\u2014\n**(1)**\nto prevent and mitigate the introduction and spread of invasive species, pests, and diseases that threaten native species;\n**(2)**\nto address the ecological consequences of climate change on native species;\n**(3)**\nto address loss and degradation of native species' habitats;\n**(4)**\nto manage, maintain, and restore populations of native species;\n**(5)**\nto increase scientific capacity to support the planning, monitoring, and research activities necessary for the conservation and recovery of native species;\n**(6)**\nto improve information collection, ecological monitoring, and management relating to the activities described in paragraphs (1) through (5); and\n**(7)**\nto engage the public through outreach, education, and community involvement to increase capacity and support for the conservation and recovery of native species in the State.\n##### (c) Development of priorities\nIn carrying out the grant program, the Secretary shall coordinate with the following individuals to develop annual, evidence-based funding priorities for the grant program that support the purposes described in subsection (b):\n**(1)**\nThe heads of Federal agencies, including\u2014\n**(A)**\nthe Administrator of the National Oceanic and Atmospheric Administration (or a designee);\n**(B)**\nthe Administrator of the Environmental Protection Agency (or a designee);\n**(C)**\nthe Secretary of Agriculture (or a designee); and\n**(D)**\nthe head of any other applicable Federal agency (or a designee), as determined by the Secretary.\n**(2)**\nThe Chairperson of the Hawaii Board of Land and Natural Resources (or a designee).\n**(3)**\nThe Chairperson of the Hawaii Board of Agriculture (or a designee).\n**(4)**\nAny other relevant stakeholder involved in the conservation and recovery of native species in the State that the Secretary determines to be appropriate.\n##### (d) Request for proposals\nThe Secretary shall publish in the Federal Register an annual request for proposals, in accordance with the funding priorities developed under subsection (c).\n##### (e) Criteria\nThe Secretary, in coordination with the individuals described in subsection (c), shall annually develop criteria for ranking project proposals to receive funding under the grant program.\n##### (f) Recusal\nIf the State or a unit of local government in the State applies for a grant under the grant program, then the individuals described in paragraphs (2), (3), and (4) of subsection (c) who are representatives of the State or that unit of local government, as applicable, shall recuse themselves from all funding decisions relating to those applications.\n##### (g) Cost sharing\n**(1) Federal share**\n**(A) In general**\nSubject to subparagraph (B), the Federal share of the cost of a project carried out under the grant program shall not exceed 75 percent.\n**(B) Exceptions**\nThe Federal share of the cost of a project carried out under the grant program may be 100 percent, as determined by the Secretary\u2014\n**(i)**\nfor any project, in the discretion of the Secretary; or\n**(ii)**\nif the project\u2014\n**(I)**\nis carried out by a Native Hawaiian organization;\n**(II)**\nsignificantly contributes to youth workforce readiness in the implementation of the project; or\n**(III)**\nis carried out using a grant awarded under the grant program in an amount of not more than $50,000.\n**(2) In-kind contributions**\nThe non-Federal share of the cost of a project carried out under the grant program may be provided in the form of an in-kind contribution of services, materials, or access to land.\n##### (h) Requirement\nOf the amounts made available to carry out the grant program for each fiscal year, not less than 5 percent shall be used to award grants for projects described in subclauses (I) through (III) of subsection (g)(1)(B)(ii).\n##### (i) Technical assistance\nThe Secretary may provide technical assistance to eligible entities to assist in the implementation of projects that receive funding under the grant program.\n##### (j) Consultation with Native Hawaiian organizations\nThe Secretary, in carrying out the grant program, shall consult with Native Hawaiian organizations with respect to any project that receives funding under the grant program with implications for the Native Hawaiian Community.\n##### (k) Supplement, not supplant\nFunds made available to carry out the grant program for each fiscal year shall supplement and not supplant other funds made available to carry out the purposes described in paragraphs (1) through (7) of subsection (b) in the State.\n#### 4. Annual report\nAnnually, the Secretary shall submit to Congress a report on the implementation of this Act, including\u2014\n**(1)**\na description of each project that has received funding under the grant program; and\n**(2)**\nthe status of each project described in paragraph (1) that is in progress on the date of submission of the applicable report.\n#### 5. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to the Secretary to carry out this Act $30,000,000 for the first fiscal year that begins after the date of enactment of this Act and for each of the 9 fiscal years thereafter.\n##### (b) Administrative expenses\nOf the amounts made available for each fiscal year under subsection (a), the Secretary shall use not more than 5 percent for administrative expenses relating to carrying out the grant program.",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "871",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Hawaii Native Species Conservation and Recovery Act of 2025",
      "type": "S"
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
        "updateDate": "2025-03-21T15:44:42Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1780ih.xml"
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
      "title": "Hawaii Native Species Conservation and Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Hawaii Native Species Conservation and Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a competitive grant program to support the conservation and recovery of native plant, fungi, and animal species in the State of Hawaii, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:31Z"
    }
  ]
}
```
