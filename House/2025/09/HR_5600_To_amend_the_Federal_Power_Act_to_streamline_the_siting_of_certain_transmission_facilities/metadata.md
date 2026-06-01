# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5600
- Title: SPEED and Reliability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5600
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-04-07T08:05:33Z
- Update date including text: 2026-04-29T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5600",
    "number": "5600",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SPEED and Reliability Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:33Z",
    "updateDateIncludingText": "2026-04-29T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:03:30Z",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "KY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5600ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5600\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Peters (for himself and Mr. Barr ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Power Act to streamline the siting of certain transmission facilities in the national interest.\n#### 1. Short title\nThis Act may be cited as the Streamlining Powerlines Essential to Electric Demand and Reliability Act of 2025 or the SPEED and Reliability Act of 2025 .\n#### 2. Transmission permitting\n##### (a) Definitions\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (a) and inserting the following:\n(a) Definitions In this section: (1) Commission The term Commission means the Federal Energy Regulatory Commission. (2) ERO The term ERO has the meaning given such term in section 215(a). (3) Improved reliability The term improved reliability means that, on balance, considering each of the matters described in subparagraphs (A) through (D), reliability is improved in a material manner that benefits customers through at least one of the following: (A) Facilitating compliance with a mandatory standard for reliability approved by the Commission under section 215. (B) A reduction in expected unserved energy, loss of load hours, or loss of load probability (as defined by the ERO). (C) Facilitating compliance with a tariff requirement or process for resource adequacy on file with the Commission. (D) Any other similar material improvement, including a reduction in correlated outage risk, such as achieved through increased geographic or resource diversification. (4) Landowner input The term landowner input means input received\u2014 (A) by the Commission; (B) from affected landowners, such as farmers and ranchers, in the path of the proposed construction or modification of an electric transmission facility; and (C) pursuant to notification provided to, and consultation with, those affected landowners, farmers, and ranchers by the Commission. (5) Secretary The term Secretary means the Secretary of Energy. .\n##### (b) Construction permit\nSection 216(b) of the Federal Power Act ( 16 U.S.C. 824p(b) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking Except and all that follows through finds that and inserting Except as provided in subsections (d)(1) and (i), the Commission shall, after notice and an opportunity for hearing, including a public comment period of at least 60 days, issue one or more permits for the construction or modification of electric transmission facilities necessary in the national interest if the Commission finds that ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)(i), by inserting or modification after siting ; and\n**(B)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting or modification after siting ; and\n**(ii)**\nin clause (i), by striking the later of in the matter preceding subclause (I) and all that follows through the semicolon at the end of subclause (II) and inserting the date on which the application was filed with the State commission or other entity; ; and\n**(3)**\nby striking paragraphs (2) through (6) and inserting the following:\n(2) the proposed facilities will be used for the transmission of electric energy in interstate (including transmission from the outer Continental Shelf to a State) or foreign commerce; (3) the proposed construction or modification is consistent with the public interest; (4) the proposed construction or modification will significantly reduce transmission congestion in interstate commerce, protect or benefit consumers, and provide improved reliability; (5) the proposed construction or modification is consistent with sound national energy policy and will enhance energy independence; (6) the electric transmission facilities are capable of transmitting electric energy at a voltage of not less than 100 kilovolts or, in the case of facilities that include advanced transmission conductors (including superconductors), as defined by the Commission, voltages determined to be appropriate by the Commission; and (7) the proposed modification (including reconductoring) will maximize, to the extent reasonable and economical, the transmission capabilities of existing towers, structures, or rights-of-way. .\n##### (c) State siting and consultation\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (d) and inserting the following:\n(d) State siting and consultation (1) Preservation of state siting authority The Commission shall have no authority to issue a permit under subsection (b) for the construction or modification of an electric transmission facility within a State except as provided in paragraph (1) of that subsection. (2) Consultation In any proceeding before the Commission under subsection (b), the Commission shall afford each State in which a transmission facility covered by the permit is or will be located, each affected Federal agency and Indian Tribe, private property owners, and other interested persons, a reasonable opportunity to present their views and recommendations with respect to the need for and impact of a facility covered by the permit. (3) Landowner input In authorizing the construction or modification of an electric transmission facility under subsection (b), the Commission shall take into account landowner input. .\n##### (d) Rights-of-Way\nSection 216(e)(3) of the Federal Power Act ( 16 U.S.C. 824p(e)(3) ) is amended by striking shall conform and all that follows through the period at the end and inserting shall be in accordance with rule 71.1 of the Federal Rules of Civil Procedure. .\n##### (e) Cost allocation\n**(1) In general**\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (f) and inserting the following:\n(f) Cost allocation (1) Transmission tariffs For the purposes of this section, any transmitting utility that owns, controls, or operates electric transmission facilities that the Commission finds to be consistent with the findings under paragraphs (2) through (6) and, if applicable, (7) of subsection (b) shall file a tariff or tariff revision with the Commission pursuant to section 205 and the regulations of the Commission allocating the costs of the new or modified transmission facilities. (2) Transmission benefits The Commission shall require that tariffs or tariff revisions filed under this subsection are just and reasonable and allocate the costs of providing service to customers that benefit, in accordance with the cost-causation principle, including through\u2014 (A) improved reliability; (B) reduced congestion; (C) reduced power losses; (D) greater carrying capacity; (E) reduced operating reserve requirements; and (F) improved access to lower cost generation that achieves reductions in the cost of delivered power. (3) Ratepayer protection Customers that receive no benefit, or benefits that are trivial in relation to the costs sought to be allocated, from electric transmission facilities constructed or modified under this section shall not be involuntarily allocated any of the costs of those transmission facilities, provided, however, that nothing in this section shall prevent a transmitting utility from recovering such costs through voluntary agreement with its customers. .\n**(2) Savings provision**\nIf the Federal Energy Regulatory Commission finds that the considerations under paragraphs (2) through (6) and, if applicable, (7) of subsection (b) of section 216 of the Federal Power Act ( 16 U.S.C. 824p ) (as amended by subsection (b)) are met, nothing in this section or the amendments made by this section shall be construed to exclude transmission facilities located on the outer Continental Shelf from being eligible for cost allocation established under subsection (f)(1) of that section (as amended by paragraph (1)).\n##### (f) Coordination of Federal authorizations for transmission facilities\nSection 216(h) of the Federal Power Act ( 16 U.S.C. 824p(h) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking the period at the end and inserting the following:\n, except that\u2014 (A) the Commission shall act as the lead agency in the case of facilities permitted under subsection (b); and (B) the Department of the Interior shall act as the lead agency in the case of facilities located on a lease, easement, or right-of-way granted by the Secretary of the Interior under section 8(p)(1)(C) of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1337(p)(1)(C) ). ;\n**(2)**\nin each of paragraphs (3), (4)(B), (4)(C), (5)(B), (6)(A), (7)(A), (7)(B)(i), (8)(A)(i), and (9), by striking Secretary each place it appears and inserting lead agency ;\n**(3)**\nin paragraph (4)(A), by striking As head of the lead agency, the Secretary and inserting The lead agency ;\n**(4)**\nin paragraph (5)(A), by striking As lead agency head, the Secretary and inserting The lead agency ; and\n**(5)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (A), by striking 18 months after the date of enactment of this section and inserting 18 months after the date of enactment of the SPEED and Reliability Act of 2025 ; and\n**(B)**\nin subparagraph (B)(i), by striking 1 year after the date of enactment of this section and inserting 18 months after the date of enactment of the SPEED and Reliability Act of 2025 .\n##### (g) Interstate compacts\nSection 216(i) of the Federal Power Act ( 16 U.S.C. 824p(i) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking , including facilities in national interest electric transmission corridors ; and\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (A), by striking ; and and inserting a period;\n**(B)**\nby striking subparagraph (B); and\n**(C)**\nby striking in disagreement in the matter preceding subparagraph (A) and all that follows through (A) the in subparagraph (A) and inserting unable to reach an agreement on an application seeking approval by the .\n##### (h) Transmission infrastructure investment\nSection 219(b)(4) of the Federal Power Act ( 16 U.S.C. 824s(b)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking and after the semicolon at the end;\n**(2)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(C) all prudently incurred costs associated with payments to jurisdictions impacted by electric transmission facilities developed pursuant to section 216. .\n##### (i) Jurisdiction\nSection 216 of the Federal Power Act ( 16 U.S.C. 824p ) is amended by striking subsection (k) and inserting the following:\n(k) Jurisdiction (1) Ercot This section shall not apply within the area referred to in section 212(k)(2)(A). (2) Other utilities (A) In general For the purposes of this section, the Commission shall have jurisdiction over all transmitting utilities, including transmitting utilities described in section 201(f), but excluding any ERCOT utility (as defined in section 212(k)(2)(B)). (B) Clarification Being subject to Commission jurisdiction for the purposes of this section shall not make an entity described in section 201(f) a public utility for the purposes of section 201(e). .\n##### (j) Conforming amendments\n**(1)**\nSection 50151(b) of Public Law 117\u2013169 ( 42 U.S.C. 18715(b) ) is amended by striking designated by the Secretary to be necessary in the national interest under section 216(a) of the Federal Power Act ( 16 U.S.C. 824p(a) ) .\n**(2)**\nSection 1222 of the Energy Policy Act of 2005 ( 42 U.S.C. 16421 ) is amended\u2014\n**(A)**\nin subsection (a)(1)(A), by striking is located in a national interest electric transmission corridor designated under section 216(a) of the Federal Power Act and ; and\n**(B)**\nin subsection (b)(1)(A), by striking is located in an area designated under section 216(a) of the Federal Power Act and .\n**(3)**\nSection 40106(h)(1)(A) of the Infrastructure Investment and Jobs Act ( 42 U.S.C. 18713(h)(1)(A) ) is amended by striking (A) is located in and all that follows through (B) is necessary in subparagraph (B) and inserting is necessary .\n##### (k) Minimizing regulatory burden\nExcept as explicitly provided, no new rule or rule making (as such terms are defined in section 551 of title 5, United States Code) shall be required of any agency in order to implement this section or any amendment made by this section.\n##### (l) Savings provision\nNothing in this section or an amendment made by this section grants authority to the Federal Energy Regulatory Commission under the Federal Power Act ( 16 U.S.C. 791a et seq. ) over sales of electric energy at retail or the local distribution of electricity.",
      "versionDate": "2025-09-26",
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
        "name": "Energy",
        "updateDate": "2025-12-17T16:47:55Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5600ih.xml"
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
      "title": "SPEED and Reliability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPEED and Reliability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Powerlines Essential to Electric Demand and Reliability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Power Act to streamline the siting of certain transmission facilities in the national interest.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T05:18:34Z"
    }
  ]
}
```
