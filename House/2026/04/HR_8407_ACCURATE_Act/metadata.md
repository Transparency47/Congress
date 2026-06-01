# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8407
- Title: ACCURATE Act
- Congress: 119
- Bill type: HR
- Bill number: 8407
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-04-28T08:06:29Z
- Update date including text: 2026-04-28T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8407",
    "number": "8407",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "ACCURATE Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:29Z",
    "updateDateIncludingText": "2026-04-28T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "RI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8407ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8407\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Scott Franklin of Florida (for himself, Mr. Amo , and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the Under Secretary of Commerce for Standards and Technology to establish a Commission on Hazard Risk Assessment Tools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Consistent and Credible Use of Risk Assessment Tools and Evaluation Act or the ACCURATE Act .\n#### 2. Commission on hazard risk assessment tools\n##### (a) Establishment\nNot later than 180 days after the enactment of this Act, the Under Secretary of Commerce for Standards and Technology shall establish a commission to be known as the Commission on Hazard Risk Assessment Tools (in this section referred to as the Commission ). The Commission shall serve in an advisory capacity and provide recommendations to the Under Secretary.\n##### (b) Duties\nThe duties of the Commission include the following:\n**(1)**\nIdentify hazard risk assessment tools and models needed and procured by Federal Departments and agencies, including\u2014\n**(A)**\nhazard maps;\n**(B)**\nflood maps;\n**(C)**\nreturn period maps;\n**(D)**\nhazard scores;\n**(E)**\nhazard ratings; and\n**(F)**\nrisk scores.\n**(2)**\nIdentify the sources of key data inputs and parameters used in the development of hazard risk assessment tools and models including\u2014\n**(A)**\ndata related to the frequency and severity of natural hazards;\n**(B)**\nscientific data related to how the frequency and severity of natural hazard affect, influence, shape risks and offsets of the built environment described in paragraph (C) and (D);\n**(C)**\ndata related to inventories of the built environment, including buildings and infrastructure;\n**(D)**\ndata related to natural hazard exposures and vulnerabilities of built environments including infrastructure, economic activity and human populations; and\n**(E)**\ndata related to the adaptation and hazard mitigation practices used to offset the risk to and impact of natural hazard exposures and vulnerabilities of built environments.\n**(3)**\nDevelop and submit to the Under Secretary of Commerce for Standards and Technology recommended standards and specifications required to validate the quality control of hazard risk assessment tools and models described in subsection (1). Such standards and specifications shall address\u2014\n**(A)**\nThe data inputs and parameters described in subsection (2);\n**(B)**\nModel assumptions; and\n**(C)**\nValidation of model outputs.\n**(4)**\nDevelop and submit to the Under Secretary of Commerce for Standards and Technology recommended standardized methodologies and protocols for the collection, validation, and analysis of the key data inputs and parameters identified in subsection (3).\n**(5)**\nCatalogue the quality, reliability, usability, timeliness, accuracy, consistency, and transparency needs for hazard risk assessment tools and models used by Federal departments and agencies that currently procure or utilize such tools, as determined by the Commission.\n**(6)**\nMake recommendations to the Under Secretary of Commerce for Standards and Technology regarding best practices for Federal departments and agencies for procurement of hazard risk assessment tools regarding the quality, reliability, usability, timeliness, accuracy, consistency, and transparency of hazard risk assessment tools and models. Such recommendations shall include an evaluation of the Federal Acquisition Regulations pertinent to such Federal departments and agencies to determine whether the current requirements should be updated based upon the recommended best practices guidance for the procurement of hazard risk assessment tools.\n**(7) Review and action**\n**(A)**\nNot later than 180 days after receiving recommendations from the Commission under this subsection, the Under Secretary of Commerce for Standards and Technology shall review such recommendations and determine whether to adopt, modify, or decline such standards, methodologies, or best practices.\n**(B)**\nThe Under Secretary for Standards and Technology may issue guidance, standards, or other appropriate directives for use by Federal departments and agencies based on such determinations.\n##### (c) Membership\n**(1) In General**\nThe Commission shall be comprised of representatives from each of the following categories.\n**(A)**\nA Federal department or agency responsible for modeling natural hazards.\n**(B)**\nA state or local emergency response organization.\n**(C)**\nFEMA.\n**(D)**\nA state regulatory agency that utilizes or procures hazard risk assessment tools or models.\n**(E)**\nA Federal department or agency that utilizes or procures hazard risk assessment tools or models.\n**(F)**\nA non-governmental organization or national association representing rural communities.\n**(G)**\nA non-governmental organization or national association representing urban communities.\n**(H)**\nInsurance industry.\n**(I)**\nBanking industry.\n**(J)**\nPublic utility industry.\n**(K)**\nConstruction industry.\n**(L)**\nReal estate industry.\n**(M)**\nTransportation/logistics.\n**(N)**\nRisk management consultant/professional.\n**(O)**\nStructural engineering.\n**(P)**\nInstitute of higher education (as such term is defined in Section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )) conducting research on hazard risk assessment tools or modeling.\n**(Q)**\nInstitute of higher education utilizing artificial intelligence (as such term is described in the National Artificial Intelligence Initiative Act of 2020 (15 U.S.C 9401)) to improve hazard risk assessment tools or models.\n**(2) Chairperson**\nThe Commission shall be chaired by the Under Secretary of Commerce for Standards and Technology or their designee.\n**(3) Appointment**\nThe Chairperson of the Commission shall appoint the members to satisfy the representational requirements described in paragraph (1).\n**(4) Expertise**\nEvery member of the Commission appointed shall all have expertise in at least one of the following categories:\n**(A)**\nEmergency management or response.\n**(B)**\nUtilization or procurement of hazard risk assessment products or models.\n**(C)**\nModeling of natural hazards.\n**(D)**\nCommunity planning.\n**(E)**\nStructural engineering with respect to natural hazards.\n**(F)**\nResearch of hazard risk assessment products or models.\n**(G)**\nUtilizing artificial intelligence to improve hazard risk assessment products or models.\n**(5) Balance**\nWhen appointing the members of the Committee, the Chairperson shall ensure at least one person with each of the expertise described in paragraph (4) is represented.\n**(6) Vacancies**\nWithin 30 days of a vacancy on the Commission occurring, the Chairperson shall fill such vacancy from the same category that created the vacancy and satisfied the requirements described in this section.\n##### (d) Conflict of interest, disclosure, and recusal\n**(1) Conflict of interest reporting**\nA member of the Commission who is not designated a Special Government Employee (SGE) shall disclose to the Chairpersons any real or potential conflict of interest if such member has a direct financial interest in any hazard risk assessment tools, model, or modeling provider that is subject to review or validation through the standards and specifications established in subsection (b)(2).\n**(2) SGE**\nA member of the Commission designated as a special government employee shall be subject to applicable laws as delineated under 18 USC 201 et Seq, Standards of Ethical Conduct for Employees of the Executive Branch.\n**(3) Disclosure protocols**\nA member of the Commission disclosing a conflict of interest in subsection (d)(1) shall submit a written report to the Commission to disclose the following:\n**(A)**\nDirect financial interest.\n**(B)**\nAffiliations with entities that have a direct financial interest.\n**(C)**\nClose relative or family member that have a direct financial interest.\n**(4) Timing of disclosure**\nDisclosure of conflict interest under subsection (1) shall occur before any meeting in which any hazard risk assessment tools, model or modeling provider is reviewed or validated.\n**(5) Recusal**\nAny member with a conflict described in subsection (2) shall seek recusal from participation in deliberations, decisions, or votes related to the review that presents the conflict.\n##### (e) Reports\nThe Commission shall submit to the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate.\n**(1)**\nA report not later than 9 months after the convening of the Commission that includes the following:\n**(A)**\nA catalogue of public and private sector sources of hazard risk assessment tools.\n**(B)**\nAn assessment of the extent to which Federal departments and agencies utilize or purchase hazard risk assessment tools or models produced by the private sector.\n**(C)**\nA list of the key inputs and parameters to hazard risk assessment tools.\n**(2)**\nA report not later than 9 months after the submission of the report in subsection (1) that includes the results of the Commission\u2019s duties outlined in section (b).\n**(3)**\nA report not later than 18 months submission of the report in subsection (2) that includes the following:\n**(A)**\nAn analysis of the results of the Commission\u2019s duties listed under section (b) regarding the efficacy of the standards and specifications in improving the quality of the hazard risk assessment tools available.\n**(B)**\nThe identification of any standards or specifications that improve the quality of the hazard risk assessment tools available or any hazard risk assessment tool that has not yet been subject to the standards and specifications.\n**(C)**\nRecommendations to address the deficiencies in existing standards and specifications and how to set standards and specifications for tools that did not fall under the purview of the original standards and specifications.\n##### (f) Utilization of hazard risk assessment tools and models\n**(1) Conditional application**\nIf the Under Secretary of Commerce for Standards and Technology adopts standards, methodologies, or guidance pursuant to subsection (b), Federal departments and agencies identified by the Commission shall, to the maximum extent practicable, incorporate such standards and guidance when procuring or utilizing hazard risk assessment tools and models from the private sector.\n**(2) Documentation**\n**(A)**\nThe purveyor of hazard risk assessment tools and models purchased in paragraph (1) shall document for Federal agencies, and provide such documentation, how such hazard risk assessment tools and models conform to the standards and specifications adopted or issued by the Under Secretary of Commerce under subsection (b). In order to qualify to sell hazard risk assessment tools and models that have undergone a material change to Federal departments and agencies, the purveyor shall document, and provide such documentation, of how the changed hazard risk assessment tools and models conform to the standards and specifications adopted or issued by the Under Secretary of Commerce under subsection (b)(7).\n**(3) Limited exceptions**\nNotwithstanding paragraph (1), a Federal department or agency may procure or utilize hazard risk assessment tools or models that do not incorporate standards or guidance issued under this subsection if:\n**(A)**\nthe Under Secretary of Commerce for Standards and Technology has not issued applicable standards or guidance for the specific use case; or\n**(B)**\nsuch procurement or use is necessary to respond to a national emergency.\n**(4) Notification**\nIf a Federal department or agency relies on paragraph (3)(B), the agency shall, not later than 30 days after such use, notify the appropriate congressional committees and provide a brief justification, as well as what steps the agency has taken to ensure that such a purchase or utilization does not recur.\n##### (g) Sunset\nThe Commission terminates 5 years after the enactment of this Act.\n##### (h) Definitions\nIn this Act:\n**(1) Built environment**\nThe term built environment means any man-made or modified structures, including associated infrastructure, that provide people with living, working, and recreational spaces.\n**(2) Hazard risk**\nThe term hazard risk means the exposure of people, property, infrastructure, or economic activity to loss or disruption resulting from variations in natural hazards over a time period of at least one year.\n**(3) Hazard risk assessment tools**\nThe term hazard risk assessment tools means products developed using hazard risk information to create output including\u2014\n**(A)**\nhazard maps;\n**(B)**\nflood maps;\n**(C)**\nreturn period maps;\n**(D)**\nhazard scores;\n**(E)**\nhazard ratings; and\n**(F)**\nrisk scores.\n**(4) Natural hazards**\nThe term natural hazards means extreme weather, water, or seismic events, including wildfire, drought, flooding, damaging winds, tornadoes, precipitation, earthquakes, and other natural phenomena, that have a high risk of loss of life or property.\n**(5) Material change**\nThe term material change means a model version update that changes underlying input data, methodology, or assumptions, or updates losses or categorization of properties or areas by more than ten percent.",
      "versionDate": "2026-04-21",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8407ih.xml"
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
      "title": "ACCURATE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T06:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCURATE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T06:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Consistent and Credible Use of Risk Assessment Tools and Evaluation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T06:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Under Secretary of Commerce for Standards and Technology to establish a Commission on Hazard Risk Assessment Tools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T06:18:29Z"
    }
  ]
}
```
