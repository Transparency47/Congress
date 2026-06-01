# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1485?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1485
- Title: North American Energy Act
- Congress: 119
- Bill type: S
- Bill number: 1485
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1485",
    "number": "1485",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "North American Energy Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-04-10T21:35:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T21:35:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1485is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1485\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Hoeven introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish a more uniform, transparent, and modern process to authorize the construction, connection, operation, and maintenance of international border-crossing facilities for the import and export of oil and natural gas and the transmission of electricity.\n#### 1. Short title\nThis Act may be cited as the North American Energy Act .\n#### 2. Approval for border-crossing facilities\n##### (a) Definitions\nIn this section:\n**(1) Appropriate Federal agencies**\nThe term appropriate Federal agencies means the Secretary of Defense, the Attorney General, the Secretary of the Interior, the Secretary of Commerce, the Secretary of Transportation, the Secretary of Energy, the Secretary of Homeland Security, the Administrator of the Environmental Protection Agency, and, for applications concerning the border with Mexico, the United States Commissioner of the International Boundary and Water Commission.\n**(2) Border-crossing facility**\nThe term border-crossing facility means\u2014\n**(A)**\nthe portion of an oil pipeline between an international boundary and the first mainline valve on the United States side of an international boundary; and\n**(B)**\nthe portion of a natural gas pipeline or electric transmission facility that is located at an international boundary of the United States.\n**(3) Electric Reliability Organization; Regional entity**\nThe terms Electric Reliability Organization and regional entity have the meanings given those terms in section 215 of the Federal Power Act ( 16 U.S.C. 824o ).\n**(4) Independent System Operator; Regional Transmission Organization**\nThe terms Independent System Operator and Regional Transmission Organization have the meanings given those terms in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(5) Modification**\nThe term modification includes a reversal of flow direction, change in ownership, change in flow volume, change in product delivered, addition or removal of an interconnection, or an adjustment to regulate flow (such as a reduction or increase in the number of pump or compressor stations or valves).\n**(6) Natural gas**\nThe term natural gas has the meaning given that term in section 2 of the Natural Gas Act ( 15 U.S.C. 717a ).\n**(7) Oil**\nThe term oil means petroleum or a petroleum product.\n##### (b) Authorization of certain energy infrastructure projects at an international boundary of the United States\n**(1) Authorization**\nExcept as provided in paragraph (3) and subsection (f), no person may construct, connect, or operate, a border-crossing facility for the import or export of oil or natural gas, or the transmission of electricity, across an international border of the United States without obtaining a certificate of crossing for the border-crossing facility under this subsection.\n**(2) Certificate of crossing**\n**(A) Requirement**\nNot later than 90 days after final action is taken, by the relevant official or agency identified under subparagraph (B), under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to a border-crossing facility for which a person requests a certificate of crossing under this subsection, the relevant official or agency, in consultation with appropriate Federal agencies, shall issue a certificate of crossing for the border-crossing facility unless the relevant official or agency finds that the construction, connection, or operation, of the border-crossing facility is not in the public interest of the United States.\n**(B) Relevant official or agency**\nThe relevant official or agency referred to in subparagraph (A) is\u2014\n**(i)**\nthe Federal Energy Regulatory Commission with respect to border-crossing facilities consisting of oil or natural gas pipelines; and\n**(ii)**\nthe Secretary of Energy with respect to border-crossing facilities consisting of electric transmission facilities.\n**(C) Additional requirement for electric transmission facilities**\nIn the case of a request for a certificate of crossing for a border-crossing facility consisting of an electric transmission facility, the Secretary of Energy shall require, as a condition of issuing the certificate of crossing under subparagraph (A), that the border-crossing facility be constructed, connected, operated, or maintained consistent with all applicable policies and standards of\u2014\n**(i)**\nthe Electric Reliability Organization and the applicable regional entity; and\n**(ii)**\nany Regional Transmission Organization or Independent System Operator with operational or functional control over the border-crossing facility.\n**(3) Exclusions**\nThis subsection shall not apply to any construction, connection, operation, or maintenance of a border-crossing facility for the import or export of oil or natural gas, or the transmission of electricity\u2014\n**(A)**\nif the border-crossing facility is operating for such import, export, or transmission as of the date of enactment of this Act;\n**(B)**\nif a permit described in subsection (e) for the construction, connection, operation, or maintenance has been issued; or\n**(C)**\nif an application for a permit described in subsection (e) for the construction, connection, operation, or maintenance is pending on the date of enactment of this Act, until the earlier of\u2014\n**(i)**\nthe date on which such application is denied; or\n**(ii)**\n2 years after the date of enactment of this Act, if such a permit has not been issued by such date.\n**(4) Effect of other laws**\n**(A) Application to projects**\nNothing in this subsection or subsection (f) shall affect the application of any other Federal statute to a project for which a certificate of crossing for a border-crossing facility is requested under this subsection.\n**(B) Natural Gas Act**\nNothing in this subsection or subsection (f) shall affect the requirement to obtain approval or authorization under sections 3 and 7 of the Natural Gas Act ( 15 U.S.C. 717b , 717f) for the siting, construction, or operation of any facility to import or export natural gas.\n**(C) Oil pipelines**\nNothing in this subsection or subsection (f) shall affect the authority of the Federal Energy Regulatory Commission with respect to oil pipelines under section 60502 of title 49, United States Code.\n**(D) Scope of NEPA review**\nNothing in this Act, or the amendments made by this Act, shall affect the scope of any review required to be conducted under section 102 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332 ) with respect to a project for which a certificate of crossing for a border-crossing facility is requested under this subsection.\n##### (c) Importation or exportation of natural gas to canada and mexico\nSection 3(c) of the Natural Gas Act ( 15 U.S.C. 717b(c) ) is amended by adding at the end the following: In the case of an application for the importation of natural gas from, or the exportation of natural gas to, Canada or Mexico, the Commission shall grant the application not later than 30 days after the date on which the Commission receives the complete application. .\n##### (d) Transmission of electric energy to Canada and Mexico\n**(1) Repeal of requirement to secure order**\nSection 202(e) of the Federal Power Act ( 16 U.S.C. 824a(e) ) is repealed.\n**(2) Conforming amendments**\n**(A) State regulations**\nSection 202(f) of the Federal Power Act ( 16 U.S.C. 824a(f) ) is amended by striking insofar as such State regulation does not conflict with the exercise of the Commission's powers under or relating to subsection (e) .\n**(B) Seasonal diversity electricity exchange**\nSection 602(b) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 824a\u20134(b) ) is amended by striking the Commission has conducted hearings and made the findings required under section 202(e) of the Federal Power Act and all that follows through the period at the end and inserting the Secretary has conducted hearings and finds that the proposed transmission facilities would not impair the sufficiency of electric supply within the United States or would not impede or tend to impede the coordination in the public interest of facilities subject to the jurisdiction of the Secretary. .\n##### (e) No presidential permit required\nNo Presidential permit (or similar permit) shall be required pursuant to any provision of law or Executive order for the construction, connection, operation, or maintenance of an oil or natural gas pipeline or electric transmission facility, or any border-crossing facility thereof.\n##### (f) Modifications to and maintenance of existing projects\nNo certificate of crossing under subsection (b), or permit described in subsection (e), shall be required for a modification to or maintenance of\u2014\n**(1)**\nan oil or natural gas pipeline or electric transmission facility that is operating for the import or export of oil or natural gas or the transmission of electricity as of the date of enactment of this Act;\n**(2)**\nan oil or natural gas pipeline or electric transmission facility for which a permit described in subsection (e) has been issued; or\n**(3)**\na border-crossing facility for which a certificate of crossing has previously been issued under subsection (b).\n##### (g) Effective dates; rulemaking deadlines\n**(1) Effective date**\nSubsections (b) through (f) and the amendments made by such subsections shall take effect on the date that is 1 year after the date of enactment of this Act.\n**(2) Rulemaking deadlines**\nEach relevant official or agency described in subsection (b)(2)(B) shall\u2014\n**(A)**\nnot later than 180 days after the date of enactment of this Act, publish in the Federal Register notice of a proposed rulemaking to carry out the applicable requirements of subsection (b); and\n**(B)**\nnot later than 1 year after the date of enactment of this Act, publish in the Federal Register a final rule to carry out the applicable requirements of subsection (b).\n##### (h) Judicial review\n**(1) In general**\nAny entity aggrieved by a final agency action taken under this section may obtain a review of such action by filing a petition for review in the United States Court of Appeals for any circuit wherein an applicant for authorization under this section is located or has its principal place of business, or in the United States Court of Appeals for the District of Columbia.\n**(2) Deadline**\nA petition for review under paragraph (1) must be filed not later than 60 days after a final agency action is taken under this section.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
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
        "name": "Energy",
        "updateDate": "2025-05-20T12:30:15Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1485is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "North American Energy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "North American Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a more uniform, transparent, and modern process to authorize the construction, connection, operation, and maintenance of international border-crossing facilities for the import and export of oil and natural gas and the transmission of electricity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:22Z"
    }
  ]
}
```
