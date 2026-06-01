# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4564?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4564
- Title: Maritime Cybersecurity Act
- Congress: 119
- Bill type: S
- Bill number: 4564
- Origin chamber: Senate
- Introduced date: 2026-05-19
- Update date: 2026-05-29T07:23:32Z
- Update date including text: 2026-05-29T07:23:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-19: Introduced in Senate
- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-05-19: Introduced in Senate

## Actions

- 2026-05-19 - IntroReferral: Introduced in Senate
- 2026-05-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-19",
    "latestAction": {
      "actionDate": "2026-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4564",
    "number": "4564",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Maritime Cybersecurity Act",
    "type": "S",
    "updateDate": "2026-05-29T07:23:32Z",
    "updateDateIncludingText": "2026-05-29T07:23:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-19",
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
        "item": {
          "date": "2026-05-19T16:09:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4564is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4564\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2026 Mr. Scott of Florida (for himself and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 46, United States Code, to require the Secretary of the department in which the Coast Guard is operating to assess cybersecurity risks of certain software and hardware used in certain maritime facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maritime Cybersecurity Act .\n#### 2. Cybersecurity vulnerability assessments of certain maritime facility software and hardware\nSection 70102 of title 46, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(C), by inserting (including, with respect to covered facilities, cybersecurity risks of covered software or hardware as provided under subsection (d)(1)) after cybersecurity risks ;\n**(B)**\nin paragraph (3), by inserting before the period , except that, for covered facilities, the Secretary shall annually update each such vulnerability assessment with respect to the identification of weaknesses in security and cybersecurity risks of covered software or hardware in accordance with subsection (d)(1) ; and\n**(C)**\nin paragraph (4)\u2014\n**(i)**\nby striking In lieu and inserting (A) Except as provided in subparagraph (B), in lieu ; and\n**(ii)**\nby adding at the end the following:\n(B) In the event that the Secretary accepts an alternative assessment described in subparagraph (A) for a covered facility, the Secretary shall still conduct an assessment under paragraph (1) of weaknesses in security and cybersecurity risks of covered software or hardware used at the facility in accordance with subsection (d)(1). ; and\n**(2)**\nby adding at the end the following:\n(d) Assessing cybersecurity risks of covered software or hardware (1) Assessments (A) In general Not later than 1 year after the date of enactment of this subsection, and annually thereafter, the Secretary, in coordination with the Director of the Cybersecurity and Infrastructure Security Agency, shall conduct an assessment under subsection (b)(1) with respect to weaknesses in security and cybersecurity risks of covered software or hardware. (B) Reducing barriers The Secretary may conduct an assessment under this paragraph\u2014 (i) notwithstanding any provision of an end user licensing agreement or other contract that would otherwise hinder such assessment; and (ii) without obtaining the consent of any owner or operator of a covered facility, or any other person, notwithstanding any other provision of law. (2) Covered facility reports and compliance (A) In general Not later than 180 days after the date of enactment of this subsection, and annually thereafter, the owner or operator of a covered facility shall submit a report to the Secretary that\u2014 (i) identifies\u2014 (I) any covered software or hardware that\u2014 (aa) the owner or operator is using, plans to use, or during the previous year used at the facility; and (bb) was manufactured\u2014 (AA) by a foreign entity of concern or a foreign country of concern; (BB) by a company controlled or operated by a foreign entity of concern or a foreign country of concern; or (CC) in a foreign country of concern; (II) any instance with respect to the facility of a cybersecurity risk resulting in a transportation security incident involving the marine transportation system or any port security system; and (III) any other cybersecurity risk with respect to the facility, without regard to whether the risk resulted in a transportation security incident; and (ii) except as provided under subparagraph (B)(ii), certifies that any covered software or hardware that the owner or operator is using, plans to use, or during the previous year used has been assessed for consistency with standards of the National Institute of Standards and Technology or equivalent standards within the previous year and the owner or operator has mitigated against any inconsistencies with such standards. (B) Compliance (i) In general Except as provided in clause (ii), the owner or operator of a covered facility may not use any covered software or hardware described in subparagraph (A)(ii) for which it cannot certify consistency with standards of the National Institute of Standards and Technology or equivalent standards. (ii) Waiver process The Secretary may issue a waiver to allow an owner or operator of a covered facility to use covered software or hardware for which it cannot certify consistency with standards of the National Institute of Standards and Technology or equivalent standards if the Secretary determines that there is low risk to national security which is outweighed by the benefit to commerce. (3) Annual reports to Congress Not later than 1 year after the date of enactment of this subsection, and annually thereafter, the Secretary, in coordination with the Director of the Cybersecurity and Infrastructure Security Agency, shall provide a report, to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives, on\u2014 (A) the findings of the most recent assessment under paragraph (1); (B) the findings of the most recent reports under paragraph (2); (C) any actions taken by the Secretary, or the Director of the Cybersecurity and Infrastructure Security Agency, to mitigate cybersecurity risks with respect to covered software or hardware; and (D) any recommendations to Congress on strengthening maritime transportation and port security with respect to cybersecurity risks of covered software or hardware. (4) Nondisclosure Subject to paragraph (5), information in any assessment or report under this subsection shall not be disclosed to the public, pursuant to section 552(b)(3) of the United States Code. (5) Coordination The Secretary shall coordinate, as appropriate, with Federal entities, and any other entities that have an agreement in effect with the Secretary for the sharing of information, to make information compiled by the Secretary under this subsection available to such entities for the purposes of maritime transportation security, cybersecurity risk mitigation, or compliance assistance related to covered facilities or covered software or hardware. (e) Definitions In this section: (1) Covered facility The term covered facility means a facility\u2014 (A) that is described in subsection (b)(1); and (B) to which part 105 or 106 of title 33, Code of Federal Regulations (or successor regulations), applies. (2) Covered software or hardware The term covered software or hardware means any software or hardware that\u2014 (A) connects to the internet or otherwise poses a cybersecurity risk; (B) is used at a covered facility; and (C) is used in\u2014 (i) the marine transportation system, including in a crane manufactured\u2014 (I) by a foreign entity of concern or a foreign country of concern; (II) by a company controlled or operated by a foreign entity of concern or a foreign country of concern; or (III) in a foreign country of concern; or (ii) a business system that, if compromised or exploited, could result in a transportation security incident; (iii) a system whose ownership, operation, maintenance, or control is delegated wholly or in part to any other party; or (iv) any other maritime infrastructure determined by the Secretary to be a high cybersecurity risk to the security of any covered facility or to maritime transportation security. (3) Cybersecurity vulnerability The term cybersecurity vulnerability means a characteristic or specific weakness that renders software or hardware or affiliated systems open to exploitation by a given threat or susceptible to a given hazard. (4) Foreign country of concern; foreign entity of concern The terms foreign country of concern and foreign entity of concern have the meanings given such terms in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) ). .",
      "versionDate": "2026-05-19",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4564is.xml"
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
      "title": "Maritime Cybersecurity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-29T07:23:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maritime Cybersecurity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-29T07:23:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 46, United States Code, to require the Secretary of the department in which the Coast Guard is operating to assess cybersecurity risks of certain software and hardware used in certain maritime facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-29T07:18:39Z"
    }
  ]
}
```
