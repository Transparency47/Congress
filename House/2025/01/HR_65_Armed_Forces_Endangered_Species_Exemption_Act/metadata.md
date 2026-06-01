# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/65?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/65
- Title: Armed Forces Endangered Species Exemption Act
- Congress: 119
- Bill type: HR
- Bill number: 65
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-12T20:32:08Z
- Update date including text: 2025-02-12T20:32:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/65",
    "number": "65",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Armed Forces Endangered Species Exemption Act",
    "type": "HR",
    "updateDate": "2025-02-12T20:32:08Z",
    "updateDateIncludingText": "2025-02-12T20:32:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:05:00Z",
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
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr65ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 65\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to further restrict the Secretary of the Interior from designating certain lands used for national defense-related purposes as critical habitat for any species under that Act and to broaden exclusions and exemptions from that Act for such defense-related purposes.\n#### 1. Short title\nThis Act may be cited as the Armed Forces Endangered Species Exemption Act .\n#### 2. Exclusion of military institutions as critical habitat\nSection 4(a)(3)(B) of the Endangered Species Act of 1973 ( 16 U.S.C. 1533(a)(3)(B) ) is amended to read as follows:\n(i) The Secretary shall not designate as critical habitat\u2014 (I) any military installation or a State-owned National Guard installation, or any portion thereof, as such terms are defined in section 100 of the Sikes Act ( 16 U.S.C. 670 ); or (II) any other lands, waters, or geographical area not described in clause (i) that is otherwise designated for use by the Secretary of Defense including by any contractor of the Department of Defense, if the Secretary of Defense determines in writing and submitted to the Secretary of the Interior that such area is necessary for military training, weapons testing, or any other reason determined appropriate by such Secretary of Defense. (ii) The Secretary of Defense shall not be required to consult with the Secretary of the Interior, under section 7(a)(2) of this Act with respect to agency action, regardless of whether the area described in clause (i) is subject to an integrated natural resources management plan prepared under section 101 of the Sikes Act ( 16 U.S.C. 670a ). .\n#### 3. Additional exclusions and exemptions from Endangered Species Act of 1973 for defense-related operations\nSection 10 of the Endangered Species Act of 1973 ( 16 U.S.C. 1539 ) is amended by adding at the end the following:\n(k) Exclusion for national defense-Related operations (1) Exclusions The prohibitions under section 9 shall not apply with respect to\u2014 (A) the taking of any endangered species or threatened species, or the importation or exportation of any such species taken as prohibited by such section, by military personnel engaged in a national defense-related operation; (B) damaging or destroying any threatened or endangered species, or removing, cutting, digging up, damaging, or destroying any such species, by military personnel engaged in a national defense-related operation; or (C) an injury to or mortality of a threatened or endangered species that results from, but is not the purpose of, a national defense-related operation, regardless of whether the operation is conducted on a military installation or other area described in section 4(a)(3)(B)(i). (2) Definitions For the purposes of this subsection\u2014 (A) the term national defense-related operation means\u2014 (i) research, development, testing, and evaluation of military munitions, other ordnance, and weapons systems; (ii) the training of members of the Armed Forces in the use and handling of military munitions, other ordnance, and weapons systems; (iii) general training and military preparedness; or (iv) any action or duty that the Secretary of Defense deems necessary to support the Department of Defense in its mission; and (B) the term military personnel means\u2014 (i) a member of the Armed Forces; and (ii) a civilian employee or contractor (including a subcontractor at any tier) of the\u2014 (I) Department of Defense (including a nonappropriated fund instrumentality of the Department); or (II) any other Federal agency, or any provisional authority, to the extent such employment relates to supporting the mission of the Department of Defense overseas. .",
      "versionDate": "2025-01-03",
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
        "name": "Environmental Protection",
        "updateDate": "2025-02-04T12:29:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr65",
          "measure-number": "65",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr65v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Armed Forces Endangered Species Exemption Act</strong></p><p>This bill establishes exemptions from the Endangered Species Act of 1973 (ESA) for defense-related operations.</p><p>First, the bill prohibits the U.S. Fish and Wildlife Service\u00a0(FWS) and the National Marine Fisheries Service (NMFS) from designating military installations or state-owned National Guard installations as critical habitat under the ESA. It also prohibits FWS and NMFS\u00a0from designating other lands, waters, or geographical areas as critical habitats if the Department of Defense (DOD) determines that the areas are necessary for military training, weapons testing, or other reasons. While DOD must submit such determinations in writing to the FWS, DOD is not required to consult with the FWS\u00a0under the ESA about such determinations.\u00a0</p><p>Next, the bill exempts military personnel\u00a0engaged in national defense-related operations (actions or duties that DOD deems necessary to support its mission) from ESA prohibitions on (1) taking (e.g., harming or killing) of\u00a0endangered species or threatened species; (2) importing or exporting such species; and (3) damaging, destroying, removing, cutting, or digging up such species. Further, the bill exempts any injury to or mortality of a threatened or endangered species that results from, but is not the purpose of, a national defense-related operation.</p><p>The term<em> military personnel </em>means\u00a0a member of the Armed Forces\u00a0as well as\u00a0a civilian employee or contractor of (1) DOD; or (2) any other federal agency,\u00a0or any provisional authority, to the extent such employment relates to supporting the mission of DOD overseas.</p>"
        },
        "title": "Armed Forces Endangered Species Exemption Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr65.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Armed Forces Endangered Species Exemption Act</strong></p><p>This bill establishes exemptions from the Endangered Species Act of 1973 (ESA) for defense-related operations.</p><p>First, the bill prohibits the U.S. Fish and Wildlife Service\u00a0(FWS) and the National Marine Fisheries Service (NMFS) from designating military installations or state-owned National Guard installations as critical habitat under the ESA. It also prohibits FWS and NMFS\u00a0from designating other lands, waters, or geographical areas as critical habitats if the Department of Defense (DOD) determines that the areas are necessary for military training, weapons testing, or other reasons. While DOD must submit such determinations in writing to the FWS, DOD is not required to consult with the FWS\u00a0under the ESA about such determinations.\u00a0</p><p>Next, the bill exempts military personnel\u00a0engaged in national defense-related operations (actions or duties that DOD deems necessary to support its mission) from ESA prohibitions on (1) taking (e.g., harming or killing) of\u00a0endangered species or threatened species; (2) importing or exporting such species; and (3) damaging, destroying, removing, cutting, or digging up such species. Further, the bill exempts any injury to or mortality of a threatened or endangered species that results from, but is not the purpose of, a national defense-related operation.</p><p>The term<em> military personnel </em>means\u00a0a member of the Armed Forces\u00a0as well as\u00a0a civilian employee or contractor of (1) DOD; or (2) any other federal agency,\u00a0or any provisional authority, to the extent such employment relates to supporting the mission of DOD overseas.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr65"
    },
    "title": "Armed Forces Endangered Species Exemption Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Armed Forces Endangered Species Exemption Act</strong></p><p>This bill establishes exemptions from the Endangered Species Act of 1973 (ESA) for defense-related operations.</p><p>First, the bill prohibits the U.S. Fish and Wildlife Service\u00a0(FWS) and the National Marine Fisheries Service (NMFS) from designating military installations or state-owned National Guard installations as critical habitat under the ESA. It also prohibits FWS and NMFS\u00a0from designating other lands, waters, or geographical areas as critical habitats if the Department of Defense (DOD) determines that the areas are necessary for military training, weapons testing, or other reasons. While DOD must submit such determinations in writing to the FWS, DOD is not required to consult with the FWS\u00a0under the ESA about such determinations.\u00a0</p><p>Next, the bill exempts military personnel\u00a0engaged in national defense-related operations (actions or duties that DOD deems necessary to support its mission) from ESA prohibitions on (1) taking (e.g., harming or killing) of\u00a0endangered species or threatened species; (2) importing or exporting such species; and (3) damaging, destroying, removing, cutting, or digging up such species. Further, the bill exempts any injury to or mortality of a threatened or endangered species that results from, but is not the purpose of, a national defense-related operation.</p><p>The term<em> military personnel </em>means\u00a0a member of the Armed Forces\u00a0as well as\u00a0a civilian employee or contractor of (1) DOD; or (2) any other federal agency,\u00a0or any provisional authority, to the extent such employment relates to supporting the mission of DOD overseas.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr65"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr65ih.xml"
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
      "title": "Armed Forces Endangered Species Exemption Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Armed Forces Endangered Species Exemption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to further restrict the Secretary of the Interior from designating certain lands used for national defense-related purposes as critical habitat for any species under that Act and to broaden exclusions and exemptions from that Act for such defense-related purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:16Z"
    }
  ]
}
```
