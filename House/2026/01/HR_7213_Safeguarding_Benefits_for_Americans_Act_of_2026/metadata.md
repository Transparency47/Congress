# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7213
- Title: Safeguarding Benefits for Americans Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7213
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-13T08:06:12Z
- Update date including text: 2026-05-13T08:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7213",
    "number": "7213",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Safeguarding Benefits for Americans Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:12Z",
    "updateDateIncludingText": "2026-05-13T08:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "CO"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7213ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7213\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Grothman (for himself, Mr. Perry , Ms. Boebert , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo restrict certain Federal assistance benefits to individuals verified to be citizens of the United States.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Benefits for Americans Act of 2026 .\n#### 2. Restricting certain Federal assistance benefits to individuals verified to be citizens\n##### (a) Restriction\n**(1) In general**\nNotwithstanding any other provision of law, an individual is not eligible for a Federal assistance benefit (as defined in paragraph (2) of this subsection) unless the individual meets the citizenship requirement specified in subsection (b)(1).\n**(2) Federal assistance Benefit**\nIn this section, the term Federal assistance benefit means, with respect to an individual, assistance furnished to the individual (or to the household, family, or other similar unit that includes the individual) under any Federal assistance program (as defined in subsection (e)), including any benefit furnished under a grant or contract made pursuant to any such program, but does not include an entity receiving a grant or contract under such a program if the grant or contract is used to furnish assistance other than to the entity receiving the grant or contract.\n##### (b) Citizenship, Attestation, and Citizenship Verification Requirements\n**(1) Citizenship requirement**\nThe citizenship requirement specified in this paragraph, with respect to an individual, is that the individual must meet\u2014\n**(A)**\nthe attestation requirement of paragraph (2); and\n**(B)**\nthe citizenship verification requirement of paragraph (3).\n**(2) Attestation requirement**\nAn individual meets the attestation requirement of this paragraph for a Federal assistance benefit if the individual has filed, in connection with the application for the benefit (or, in the case of an individual who is a recipient of the benefit, filed with the provider of the benefit), a declaration in writing (under penalty of perjury and in a form and manner specified under subsection (c)(3)) that the individual is a citizen or national of the United States.\n**(3) Citizenship verification requirement**\n**(A) In general**\nAn individual meets the citizenship verification requirement of this paragraph\u2014\n**(i)**\nin connection with an application for a Federal assistance benefit, if the individual\u2014\n**(I)**\nfurnishes in connection with the application satisfactory documentary evidence (as defined in section 1903(x)(3) of the Social Security Act ( 42 U.S.C. 1396b(x)(3) )) of United States citizenship or nationality;\n**(II)**\nfurnishes in connection with the application a photographic identity document described in section 274A(b)(1)(D) of the Immigration and Nationality Act; and\n**(III)**\nfurnishes in connection with the application the individual\u2019s name and social security account number and has the name and number and citizenship or nationality status confirmed in accordance with subparagraphs (B)(ii) and (C)(ii) as being consistent with information in the records maintained by the Commissioner of Social Security or the Secretary of Homeland Security, respectively; or\n**(ii)**\nin the case of a recipient of a Federal assistance benefit, if the individual furnishes to the provider of the benefit the documentary evidence and other information described in clause (i), and has the individual\u2019s name and social security account number and social security number and citizenship or nationality status confirmed as described in clause (i)(III).\n**(B) Confirmation through social security**\n**(i) Transmittal of ssn to ssa**\nAn entity that is furnished a name, social security account number, and other identity information for an individual under subparagraph (A) shall submit the name and number to the Commissioner of Social Security for confirmation under clause (ii) of this subparagraph.\n**(ii) Confirmation or nonconfirmation by ssa**\nUpon receipt of a submittal under clause (i) from an entity, the Commissioner shall compare the information submitted with the information in the records maintained by the Commissioner and transmit to the entity either a confirmation or nonconfirmation as to whether the number submitted is valid and whether the information in the Social Security Administration indicates that the individual is a citizen or national of the United States.\n**(C) Confirmation through dhs**\n**(i) Transmittal to dhs**\nAn entity that is furnished a name and social security account number and other identity information for an individual under subparagraph (A) of this paragraph shall submit the name and number and such other identifying information as the Director may require under subsection (c)(3)(B) respecting the individual to the Secretary of Homeland Security for confirmation under clause (ii) of this subparagraph.\n**(ii) Review and confirmation or nonconfirmation by dhs**\nUpon receipt of a submittal under clause (i) from an entity, the Secretary of Homeland Security shall transmit to the entity either a confirmation or nonconfirmation as to whether the information in the records of the Department of Homeland Security indicates that the individual is a citizen or national of the United States.\n**(D) Verification through save program**\nAn entity that is furnished a name and social security account number and other identity information for an individual under subparagraph (A) shall verify that the individual is not included as a noncitizen in the Systematic Alien Verification for Entitlements (SAVE) Program of the Department of Homeland Security.\n**(E) Notice**\nIn the case of an individual who does not provide the documentary evidence referred to in subparagraph (A) or who does not receive confirmation of United States citizenship or nationality under subparagraph (B)(ii) or (C)(ii), the entity processing the application for, or providing, the Federal assistance benefit involved shall notify the individual of the individual\u2019s ineligibility under this section with respect to the benefit, and of the opportunity of the individual to appeal the ineligibility determination.\n**(F) Appeals process**\nThe head of any department or agency of the Federal Government who is administering a Federal benefit program shall provide a process through which an individual may appeal a determination made under this Act that an individual is ineligible for a Federal assistance benefit.\n**(4) National defined**\nIn this section, the term national means a national of the United States (as defined in section 101(a)(22) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(22) )).\n##### (c) Additional Rules; Administration\n**(1) Treatment of certain families and households**\nIn the case of a Federal assistance benefit which is made available based on\u2014\n**(A)**\neligibility for a child, the child shall be treated as meeting the citizenship requirement of subsection (b)(1) if the child, or a parent or legal guardian of the child, meets the requirement; and\n**(B)**\neligibility for a household or other family unit, the members of the household or family unit shall be treated as meeting the citizenship requirement if any individual who is treated as a member of the household or family unit meets the requirement, except that\u2014\n**(i)**\nif the program under which the benefit is furnished is the program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ), the citizenship requirement must be met by an elderly individual who is a member of the household; and\n**(ii)**\nif the program under which the benefit is furnished is the program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ), the citizenship requirement must be met by a disabled individual who is a member of the household.\n**(2) Satisfaction of requirement**\nOnce an individual meets the citizenship requirement of subsection (b)(1) with respect to a Federal assistance benefit, the individual shall be treated as continuing to meet the requirement for the benefit so long as the individual otherwise remains continuously eligible for the benefit.\n**(3) General administration**\n**(A) In general**\nThe Director of the Office of Management and Budget may issue such regulations and guidance as may be required to carry out this section.\n**(B) Specifications of declaration form and verification process**\nNot later than 30 days after the date of the enactment of this Act, the Director shall specify the form and manner of the declaration of citizenship form under subsection (b)(2) and the method for verifying citizenship to be used under subsection (b)(3) consistent with the following:\n**(i)**\nThe declaration form shall be based on the declaration form used for purposes of section 1137(d)(1)(A) of the Social Security Act ( 42 U.S.C. 1320b\u20137(d)(1)(A) ).\n**(ii)**\nThe verification process described in subparagraphs (A), (B), and (C) of subsection (b)(3) shall be based on the process used for purposes of paragraphs (1) and (2) of section 1902(ee) of the Social Security Act ( 42 U.S.C. 1396a(ee) ).\n**(4) Superseding other citizenship-related eligibility requirements**\nThe provisions of this section supersede any provisions of law relating to the eligibility for Federal assistance benefits of individuals based on citizenship, nationality, or immigration status, unless the Director of the Office of Management and Budget determines that the provisions of the law are more restrictive than the requirements of this section.\n##### (d) Disqualification for Willful and Repeated Noncompliance\n**(1) In general**\nIf the Director of the Office of Management and Budget determines that an entity providing a Federal assistance benefit has willfully and repeatedly furnished the benefit to individuals who have not met the citizenship requirement of subsection (b)(1) or has willfully and repeatedly failed to submit information as required under subparagraph (B)(i) or (C)(i) of subsection (b)(3), the entity is disqualified from furnishing the benefit, and the Director shall add the name of the entity to the List of Excluded Individuals/Entities, until the Director determines that any such benefit furnished to any such individual has been recovered.\n**(2) Monitoring of programs by the inspectors general**\nThe Inspector General for the respective Federal Department or agency with primary responsibility for a Federal assistance program shall provide for regular reports on compliance of the entities furnishing benefits under the program in applying subsection (a).\n##### (e) Federal Assistance Program Defined\nIn this section, the term Federal assistance program \u2014\n**(1)**\nmeans any provision of Federal law (other than the Internal Revenue Code of 1986 or any other Federal law pertaining to taxation) that authorizes a benefit to be furnished for which eligibility is based in whole or in part on the income or resources of the beneficiary; and\n**(2)**\nincludes any provision of the Social Security Act that authorizes a benefit to be furnished.\n##### (f) Effective Date\n**(1) In general**\nSubsection (a) shall apply to determinations (including redeterminations) of eligibility made on or after the date that is 1 year after the date of the enactment of this Act.\n**(2) Transition rule**\nIn no case shall an individual remain eligible for a Federal assistance benefit after the date that is 2 years after the date of the enactment of this Act without satisfying the citizenship requirement of subsection (b)(1).",
      "versionDate": "2026-01-22",
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
        "name": "Social Welfare",
        "updateDate": "2026-02-18T15:38:20Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7213ih.xml"
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
      "title": "Safeguarding Benefits for Americans Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Benefits for Americans Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict certain Federal assistance benefits to individuals verified to be citizens of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:41Z"
    }
  ]
}
```
