# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2988?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2988
- Title: VITAL Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2988
- Origin chamber: Senate
- Introduced date: 2025-10-08
- Update date: 2026-03-10T11:03:23Z
- Update date including text: 2026-03-10T11:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-08: Introduced in Senate
- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-10-08: Introduced in Senate

## Actions

- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2988",
    "number": "2988",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "VITAL Act of 2025",
    "type": "S",
    "updateDate": "2026-03-10T11:03:23Z",
    "updateDateIncludingText": "2026-03-10T11:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-08",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-08",
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
            "date": "2025-10-08T17:35:47Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-08T17:35:47Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2988is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2988\nIN THE SENATE OF THE UNITED STATES\nOctober 8, 2025 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo bolster upgrades and infrastructure for lasting development at the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Veterans' Infrastructure and Transformation Act of 2025 or the VITAL Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Modification of authority for sharing of health-care resources of Department of Veterans Affairs to include flexible space utilization and streamlined service agreements.\nSec. 3. Use of commercial construction and facilities code and standards.\nSec. 4. Exchanges of real property via enhanced-use lease.\nSec. 5. Pilot program on authority of Secretary of Veterans Affairs to enter into enhanced-use leases for noncash consideration.\nSec. 6. Feasibility studies for outleasing facilities of Department of Veterans Affairs.\nSec. 7. Report on strategic plan for infrastructure and capital assets of Department of Veterans Affairs.\nSec. 8. Contracting for construction project management services.\nSec. 9. Expansion and extension of pilot program on acceptance by the Department of Veterans Affairs of donated facilities and related improvements.\nSec. 10. Reforming requirements and authorities of Director of Construction and Facilities Management of Department of Veterans Affairs.\nSec. 11. Consolidation of construction and leasing activities of Department of Veterans Affairs.\nSec. 12. Consolidation of Department of Veterans Affairs acquisition, procurement, and logistics.\nSec. 13. Reports to Congress.\nSec. 14. General limitation on obligations.\n#### 2. Modification of authority for sharing of health-care resources of Department of Veterans Affairs to include flexible space utilization and streamlined service agreements\nSection 8153 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(3)\u2014\n**(A)**\nin subparagraph (A), by inserting physical before space ;\n**(B)**\nin subparagraph (B)(i), by inserting physical before space ;\n**(C)**\nby striking subparagraph (E);\n**(D)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (D) and (E), respectively;\n**(E)**\nby inserting after subparagraph (B) the following new subparagraph (C):\n(C) If the health-care resource required is physical space or common services and is to be acquired from an institution affiliated with the Department in accordance with section 7302 of this title or another entity, the Secretary may make arrangements, by contract, resource-sharing agreement, space-sharing agreement, or other form of agreement, for the acquisition of the space or service\u2014 (i) without regard to any law or regulation (including any Executive order, circular, or other administrative policy) that would otherwise require the use of competitive procedures for acquiring the resource; and (ii) if all obligations are funded through available appropriations or borne by the institution or entity, without regard to any limitations applicable to leases of the Department. ;\n**(F)**\nin subparagraph (D), as redesignated by subparagraph (D) of this paragraph, by striking subparagraph (A) or (B) and inserting subparagraph (A), (B), or (C) ; and\n**(2)**\nby adding at the end the following:\n(h) In this section: (1) The term commercial service means a service that is offered and sold competitively in the commercial marketplace, is performed under standard commercial terms and conditions, and is procured using firm-fixed price contracts. (2) The term common service means a commercial service necessary to maintain or operate physical space, including maintenance, heating, ventilation, air conditioning, electricity, energy, water, wastewater, landscaping, security, laundry, or any other service as determined by the Secretary. (3) The term physical space means one or more buildings, a portion of a building, or parking facilities. .\n#### 3. Use of commercial construction and facilities code and standards\n##### (a) In general\nThe Secretary of Veterans Affairs may use commercial codes and standards instead of or in addition to Federal codes and standards in the construction or alteration of facilities of the Department of Veterans Affairs.\n##### (b) Pilot projects\nThe Secretary shall undertake not fewer than 3 pilot projects during each of fiscal years 2027, 2028, 2029, 2030, and 2031 utilizing commercial codes and standards instead of Federal codes and standards to lease or construct facilities of the Department.\n##### (c) Reports\nThe Secretary shall submit a report to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives not later than 90 days after the end of each of fiscal years 2027, 2028, 2029, 2030, and 2031 detailing the use by the Secretary of the authority provided by subsection (a) and conduct of each pilot project required by subsection (b) that was initiated, ongoing, or completed during the fiscal year.\n##### (d) Definitions\nIn this section:\n**(1)**\nThe term commercial codes and standards means building codes or standards of the following:\n**(A)**\nThe National Fire Protection Association.\n**(B)**\nThe International Code Council.\n**(C)**\nThe American Society for Testing and Materials.\n**(D)**\nThe American Society of Civil Engineers.\n**(E)**\nThe State or local jurisdiction in which the facility of the Department for which the Secretary is applying the authority in subsection (a) is located.\n**(2)**\nThe term Federal codes and standards means the following:\n**(A)**\nThe Technical Information Library of the Department.\n**(B)**\nThe Unified Facilities Criteria of the Department of Defense.\n**(C)**\nBuilding codes or standards of Federal agencies other than the Department.\n#### 4. Exchanges of real property via enhanced-use lease\nSection 8162(b) of title 38, United States Code, is amended by striking paragraphs (2) through (6) and inserting the following:\n(3) (A) For any enhanced-use lease entered into by the Secretary, the lease consideration provided to the Secretary shall consist solely of cash at fair value as determined by the Secretary, except in the case of an exchange of leased properties assessed to be of similar value. (B) The Secretary may enter into an enhanced-use lease without receiving consideration. (C) The Secretary may not waive or postpone the obligation of a lessee to pay any consideration under an enhanced-use lease, including monthly rent. (4) The terms of an enhanced-use lease may provide for the Secretary to use minor construction funds for capital contribution payments. (5) The Office of Management and Budget shall review each enhanced-use lease before the lease goes into effect. .\n#### 5. Pilot program on authority of Secretary of Veterans Affairs to enter into enhanced-use leases for noncash consideration\n##### (a) Pilot program required\nThe Secretary of Veterans Affairs shall carry out a pilot program to assess the feasibility and advisability of entering into enhanced-use leases for noncash consideration.\n##### (b) Enhanced-Use leases\nUnder the pilot program required by subsection (a), the Secretary shall enter into at least one enhanced-use lease, but not more than three enhanced-use leases, under section 8162 of title 38, United States Code.\n##### (c) Locations\nThe enhanced-use leases entered into under the pilot program required by subsection (a) shall be in such locations as the Secretary considers appropriate for purposes of the pilot program.\n##### (d) Consideration\n**(1) In general**\nNotwithstanding paragraphs (3)(A), (3)(B), and (5) of section 8162(b) of such title and subject to the availability of appropriations and the provisions of this subsection, for an enhanced-use lease entered into by the Secretary under the pilot program required by subsection (a), the lease consideration provided to the Secretary may consist of noncash consideration at fair value as determined by the Secretary.\n**(2) Limitations**\nNoncash consideration received for an enhanced-use lease under the pilot program required by subsection (a) may consist of only the following:\n**(A)**\nTitle transfer of real property.\n**(B)**\nInfrastructure improvements.\n**(C)**\nDesign services.\n**(D)**\nConstruction services.\n**(3) Requirements**\nThe authority to accept consideration described in paragraph (1) shall be subject to the following:\n**(A)**\nAny facility accepted as noncash consideration for an enhanced-use lease is substantially complete within 10 years of entering into the enhanced-use lease, excluding commissioning and warranty services.\n**(B)**\nThe partner entity assumes full responsibility for all maintenance, operations, and service costs associated with noncash consideration for the duration of the enhanced-use lease and any subsequent use by the Department, unless explicitly funded through appropriations.\n##### (e) Capital Asset Fund\nNotwithstanding section 8118(b)(3) of title 38, United States Code, amounts in the Department of Veterans Affairs Capital Asset Fund may be used for enhanced-use leases under the pilot program required by subsection (a) for the purposes of subparagraph (C) of such section, without reference to the amount limitation in section 8104(a)(3)(A) of such title, if such use is subject to the availability of appropriations.\n##### (f) Fiscal oversight and reporting\n**(1) In general**\nFor each fiscal year, not later than 90 days after the last day of the fiscal year, the Secretary shall submit to Congress a report on the enhanced-use leases entered into under the pilot program required by subsection (a) that were in effect in that fiscal year.\n**(2) Contents**\nEach report submitted pursuant to paragraph (1) shall include, for the fiscal year covered by the report, the following:\n**(A)**\nDetails of the fiscal impact of each enhanced-use lease entered into under the pilot program required by subsection (a) that was in effect, including the following:\n**(i)**\nComprehensive budget justification for all obligations incurred.\n**(ii)**\nThe funding sources for such obligations.\n**(iii)**\nConfirmation that all associated costs are within appropriated budgets.\n**(B)**\nAn assessment of any potential future costs and mitigation strategies to ensure compliance with discretionary funding.\n##### (g) Limitation on obligations\nNo enhanced-use lease under the pilot program required by subsection (a) shall impose a financial or operational obligation on the Department beyond the availability of appropriations, and any agreement regarding an enhanced-use lease shall include a provision ensuring that maintenance, operations, or service costs associated with noncash consideration is borne by the partner entity or explicitly funded through appropriations for the entire lifecycle of the enhanced-use lease or facility use.\n##### (h) Sunset\nThe authorities provided under this section shall terminate on the date that is seven years after the date of the enactment of this Act. Such termination shall not affect the validity or terms of an enhanced-use lease entered into under this section, consideration accepted under this section, or the availability of amounts for an enhanced-use lease, provided that all obligations remain subject to the availability of appropriations.\n##### (i) Definition of enhanced-Use lease\nIn this section, the term enhanced-use lease has the meaning given such term in section 8162(a)(1) of title 38, United States Code.\n#### 6. Feasibility studies for outleasing facilities of Department of Veterans Affairs\n##### (a) In general\nThe Secretary of Veterans Affairs, subject to the availability of funds for such purposes, may conduct feasibility studies to evaluate the potential outleasing of existing medical facilities of the Department of Veterans Affairs to generate resources, including in-kind consideration such as the construction of new facilities at alternative locations, to meet current and future health care needs of veterans.\n##### (b) Elements\nEach feasibility study conducted under subsection (a) shall\u2014\n**(1)**\nassess the financial, operational, and strategic impacts of outleasing medical facilities of the Department, including the potential for reinvesting proceeds or in-kind contributions into new or modernized facilities of the Department; and\n**(2)**\nconsider that any resulting obligations in connection with such outleasing shall be funded through appropriations or borne by the partner entity for the entire lifecycle of the outleasing arrangement.\n##### (c) Report\nNot later than one year after conducting any feasibility study under subsection (a), the Secretary shall submit to Congress a report detailing\u2014\n**(1)**\nthe findings of the Secretary with respect to such study;\n**(2)**\nthe recommendations of the Secretary for potential outleasing arrangements pursuant to such study; and\n**(3)**\na budget justification confirming that all costs for such arrangements are within appropriated funds or covered by the partner entity.\n#### 7. Report on strategic plan for infrastructure and capital assets of Department of Veterans Affairs\n##### (a) Report\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives a report on the strategic plan for infrastructure and capital assets of the Department of Veterans Affairs, which summarizes a facility lifecycle strategy targeting modernization of owned and leased facilities and infrastructure required to mitigate increasing systemic failures, veteran and staff safety, benefits delivery interruptions, and funding associated to address emergency repairs.\n##### (b) Elements\nThe report required by subsection (a) shall cover known and projected requirements over a period of not less than 10 years for the following:\n**(1)**\nLand acquisition.\n**(2)**\nOperations and maintenance of facilities of the existing capital asset portfolio of the Department.\n**(3)**\nOperations and maintenance of the planned future capital asset portfolio of the Department.\n**(4)**\nNew construction, disaggregated by type of new construction, including the following types of construction:\n**(A)**\nMajor construction.\n**(B)**\nMinor construction.\n**(C)**\nNonrecurring maintenance.\n**(5)**\nLeasing.\n**(6)**\nAlternative acquisition methods, such as partnerships and donations.\n**(7)**\nActivation of space.\n**(8)**\nDisposal, reuse, and remediation.\n**(9)**\nFacility lifecycle strategy process supporting the planning, programming delivery, management, and maintenance of the current and future capital asset portfolio of the Department.\n**(10)**\nA discussion of the negative effect of the lack of stable and predictable capital asset funding on the ability of the Department to plan, staff, and execute effective capital asset management.\n**(11)**\nSuch other matters as the Secretary considers appropriate, including with respect to legislative or administrative action, provided such actions are subject to the availability of appropriated funds.\n##### (c) Rule of construction\nNothing in this section or a report submitted under this section shall be construed to create or imply any financial or operational obligation beyond the availability of appropriated funds.\n#### 8. Contracting for construction project management services\nSubject to the availability of appropriations, the Secretary of Veterans Affairs may contract with private entities for comprehensive construction project management services, including the provision of entire project teams. Such teams shall be led by an official designated by the Secretary, and the services shall be treated as a contracted service rather than individual personnel hires.\n#### 9. Expansion and extension of pilot program on acceptance by the Department of Veterans Affairs of donated facilities and related improvements\n##### (a) Expansion\n**(1) In general**\nSubsection (a)(1) of section 2 of the Communities Helping Invest through Property and Improvements Needed for Veterans Act of 2016 ( Public Law 114\u2013294 ; 38 U.S.C. 8103 note) is amended\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking property ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(C) A minor construction or nonrecurring maintenance project of the Department. .\n**(2) Conforming amendments**\nSuch section is further amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin the heading, by striking of property ;\n**(ii)**\nin the matter preceding paragraph (1), by striking the donation of a property and inserting a donation ;\n**(iii)**\nin paragraph (1)\u2014\n**(I)**\nby inserting or project after property each place it appears; and\n**(II)**\nin subparagraph (B)(ii), by inserting or the five-year development plan of the Department after priority list ; and\n**(iv)**\nin paragraph (2), by inserting project, after improvements, ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nin the matter preceding subparagraph (A), by striking real property and improvements donated under the pilot program and inserting a donation ;\n**(II)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(III)**\nin subparagraph (B)(ii), by striking the period at the end and inserting ; or ; and\n**(IV)**\nby adding at the end the following new subparagraph:\n(C) the performance of a minor construction or nonrecurring maintenance project of the Department. ; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nin subparagraph (A), by striking construction of the facility and inserting donation ;\n**(II)**\nin subparagraph (B), by inserting maintaining, after altering, ; and\n**(III)**\nin subparagraph (C), by striking construction of the facility and inserting donation ;\n**(C)**\nin subsection (e)(1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby inserting alter, maintain, after design, ;\n**(II)**\nby striking real property and improvements donated and inserting a donation ; and\n**(III)**\nby striking of the real property and improvements ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nin the matter preceding clause (i), by inserting alter, maintain, after design, ; and\n**(II)**\nin clause (ii)(I), by striking construction and donation of the real property and improvements and inserting donation ; and\n**(D)**\nin subsection (g)\u2014\n**(i)**\nin paragraph (1)\u2014\n**(I)**\nby striking real property and improvements donated and inserting donations ; and\n**(II)**\nby striking that property and inserting that donation ; and\n**(ii)**\nin paragraph (2)\u2014\n**(I)**\nby striking of real property and improvements conducted ; and\n**(II)**\nby striking that property and inserting those donations .\n##### (b) Extension\nSuch section is further amended, in subsection (i), by striking December 16, 2026 and inserting December 16, 2031 .\n#### 10. Reforming requirements and authorities of Director of Construction and Facilities Management of Department of Veterans Affairs\nSection 312A of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(4), by inserting , the Under Secretary for Health, and the Chief Acquisition Officer after Deputy Secretary ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Supervision of employees (1) All employees of the Department engaged in the following activities shall report to the Director of Construction and Facilities Management: (A) Planning, design, and construction of facilities and infrastructure of the Department, including major medical facility projects and minor medical facility projects. (B) Developing and updating short-range and long-range strategic capital investment strategies and plans of the Department. (C) Leasing of real property by the Department, including short-term, long-term, major medical facility leases, and minor medical facility leases. (D) Repair, maintenance, and operation of facilities of the Department, including custodial services, building management and administration, and maintenance of roads, grounds, and infrastructure. (E) Procurement and acquisition of major medical facility projects, minor medical facility projects, major medical facility leases, minor medical facility leases, operation, design, furnishing, and supplies and equipment. (2) In this subsection: (A) The term major medical facility lease has the meaning given such term in section 8104(a)(3) of this title. (B) The term major medical facility project has the meaning given such term in section 8104(a)(3) of this title. (C) The term minor medical facility project means a project for the construction, alteration, or acquisition of a medical facility that is not a major medical facility project. (D) The term minor medical facility lease means a lease for space for uses as a new medical facility that is not a major medical facility lease. .\n#### 11. Consolidation of construction and leasing activities of Department of Veterans Affairs\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall\u2014\n**(1)**\nconsolidate the functions of the Veterans Benefits Administration, the Veterans Health Administration, and the National Cemetery Administration described in subsection (c) of section 312A of title 38, United States Code, under the Director of Construction and Facilities Management;\n**(2)**\nconsolidate the employees of the Veterans Benefits Administration, the Veterans Health Administration, and the National Cemetery Administration described in subsection (d) of such section, as added by section 3, under the Director of Construction and Facilities Management; and\n**(3)**\nas a component of the regional organizational structure described in section 5(b), establish a regional organizational structure for the employees described in paragraph (2) reporting to the Director of Construction and Facilities Management.\n#### 12. Consolidation of Department of Veterans Affairs acquisition, procurement, and logistics\n##### (a) Organizational consolidation\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall organizationally consolidate under the Chief Acquisition Officer of the Department of Veterans Affairs (designated in accordance with section 1702 of title 41, United States Code) the functions of the Veterans Benefits Administration, the Veterans Health Administration, and the National Cemetery Administration relating to\u2014\n**(1)**\nacquisition;\n**(2)**\nprocurement and contracting;\n**(3)**\nlogistics; and\n**(4)**\nthe administration of chapter 81 of title 38, United States Code.\n##### (b) Regional organizational structure\n**(1) Establishment required**\nThe Secretary shall establish a regional organizational structure for the employees performing the functions described in subsection (a) reporting to the Chief Acquisition Officer of the Department.\n**(2) Requirements**\nThe regional organizational structure established pursuant to paragraph (1) shall\u2014\n**(A)**\ncorrespond in part or in whole to the boundaries of the Veterans Integrated Service Networks of the Veterans Health Administration;\n**(B)**\nmay include overarching or constituent organizational structures; and\n**(C)**\nmay include dedicated offices for the Veterans Benefits Administration or National Cemetery Administration.\n**(3) Regional directors**\n**(A) Regional directors of acquisition, logistics, and construction**\n**(i) In general**\nThe Secretary shall ensure that each region within the organizational structure established pursuant to paragraph (1) is headed by a regional director of acquisition, logistics, and construction reporting to the Chief Acquisition Officer of the Department responsible for supervising the functions described in (a).\n**(ii) Career reserved positions**\nEach regional director described in clause (i) shall be a career reserved position, as such term is defined in section 3132(a) of title 5, United States Code.\n**(iii) Selection**\nRegional directors described in clause (i) may be selected from among current employees of the Department performing functions described in subsection (a).\n**(B) Regional directors of construction and leasing**\nThe Secretary shall ensure that each region within the organizational structure established pursuant to paragraph (1) includes a regional director of construction and leasing who\u2014\n**(i)**\nreports to the regional director of acquisition, logistics, and construction heading the region pursuant to subparagraph (A); and\n**(ii)**\nis responsible for supervising the employees for the region described in section 4(2).\n##### (c) Relocation\nSubsection (a) shall not be construed to require the physical relocation of employees of the Department.\n#### 13. Reports to Congress\n##### (a) Report on use of additional authorities relating to recruitment and retention of personnel\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the appropriate committees of Congress a report detailing how the Secretary will use the authorities of section 706 of title 38, United States Code, to increase the size and performance of the acquisition workforce of the Department of Veterans Affairs.\n##### (b) Report on consolidation activities\nNot later than 390 days after the date of the enactment of this Act, the Secretary shall submit to the appropriate committees of Congress a report detailing how sections 11 and 12 were implemented.\n##### (c) Definitions\nIn this section:\n**(1) Acquisition workforce of the Department**\nThe term acquisition workforce of the Department of Veterans Affairs means personnel of the Department of Veterans Affairs occupying positions within the 1102 occupational series as defined by the Director of the Office of Personnel Management.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives.\n#### 14. General limitation on obligations\nNo provision of this Act shall authorize or permit the Secretary of Veterans Affairs to incur financial or operational obligations, including but costs for construction, leasing, maintenance, operations, or services, beyond the availability of funds appropriated by Congress. All agreements, contracts, or arrangements entered into under this Act shall include provisions ensuring compliance with this limitation.",
      "versionDate": "2025-10-08",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-17T16:33:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-08",
    "originChamber": "Senate",
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
          "measure-id": "id119s2988",
          "measure-number": "2988",
          "measure-type": "s",
          "orig-publish-date": "2025-10-08",
          "originChamber": "SENATE",
          "update-date": "2026-02-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2988v00",
            "update-date": "2026-02-23"
          },
          "action-date": "2025-10-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans' Infrastructure and Transformation Act of 2025 or the VITAL Act of 2025</strong></p><p>This bill addresses various policies and procedures related to Department of Veterans Affairs (VA) infrastructure and facilities, including those related to construction projects.</p><p>The bill modifies the VA\u2019s authority to share health care resources, including by providing for a simplified agreement process to share physical space (e.g., a building or parking facility) or common services (e.g., electricity).</p><p>The bill also modifies the VA\u2019s authority to lease its real property (enhanced-use leases). Specifically, the bill allows for the exchange of real property that is assessed to be of similar value and removes the cap on the length of an enhanced-use lease. The bill\u00a0requires the VA to implement a seven-year pilot program to assess the feasibility and advisability of entering into enhanced-use leases for noncash consideration.</p><p>Among other elements, the bill also</p><ul><li>authorizes the VA to use commercial codes and standards instead of or in addition to federal codes and standards in constructing or altering VA facilities,</li><li>authorizes the VA to contract with private entities for comprehensive construction project management services,</li><li>expands and extends the pilot program under which the VA may accept donations of real property and facilities,</li><li>modifies the authority and responsibilities of the VA\u2019s Director of Construction and Facilities Management, and</li><li>requires the VA to consolidate certain employees and functions relating to facilities and infrastructure as well as acquisition and procurement.</li></ul>"
        },
        "title": "VITAL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2988.xml",
    "summary": {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans' Infrastructure and Transformation Act of 2025 or the VITAL Act of 2025</strong></p><p>This bill addresses various policies and procedures related to Department of Veterans Affairs (VA) infrastructure and facilities, including those related to construction projects.</p><p>The bill modifies the VA\u2019s authority to share health care resources, including by providing for a simplified agreement process to share physical space (e.g., a building or parking facility) or common services (e.g., electricity).</p><p>The bill also modifies the VA\u2019s authority to lease its real property (enhanced-use leases). Specifically, the bill allows for the exchange of real property that is assessed to be of similar value and removes the cap on the length of an enhanced-use lease. The bill\u00a0requires the VA to implement a seven-year pilot program to assess the feasibility and advisability of entering into enhanced-use leases for noncash consideration.</p><p>Among other elements, the bill also</p><ul><li>authorizes the VA to use commercial codes and standards instead of or in addition to federal codes and standards in constructing or altering VA facilities,</li><li>authorizes the VA to contract with private entities for comprehensive construction project management services,</li><li>expands and extends the pilot program under which the VA may accept donations of real property and facilities,</li><li>modifies the authority and responsibilities of the VA\u2019s Director of Construction and Facilities Management, and</li><li>requires the VA to consolidate certain employees and functions relating to facilities and infrastructure as well as acquisition and procurement.</li></ul>",
      "updateDate": "2026-02-23",
      "versionCode": "id119s2988"
    },
    "title": "VITAL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans' Infrastructure and Transformation Act of 2025 or the VITAL Act of 2025</strong></p><p>This bill addresses various policies and procedures related to Department of Veterans Affairs (VA) infrastructure and facilities, including those related to construction projects.</p><p>The bill modifies the VA\u2019s authority to share health care resources, including by providing for a simplified agreement process to share physical space (e.g., a building or parking facility) or common services (e.g., electricity).</p><p>The bill also modifies the VA\u2019s authority to lease its real property (enhanced-use leases). Specifically, the bill allows for the exchange of real property that is assessed to be of similar value and removes the cap on the length of an enhanced-use lease. The bill\u00a0requires the VA to implement a seven-year pilot program to assess the feasibility and advisability of entering into enhanced-use leases for noncash consideration.</p><p>Among other elements, the bill also</p><ul><li>authorizes the VA to use commercial codes and standards instead of or in addition to federal codes and standards in constructing or altering VA facilities,</li><li>authorizes the VA to contract with private entities for comprehensive construction project management services,</li><li>expands and extends the pilot program under which the VA may accept donations of real property and facilities,</li><li>modifies the authority and responsibilities of the VA\u2019s Director of Construction and Facilities Management, and</li><li>requires the VA to consolidate certain employees and functions relating to facilities and infrastructure as well as acquisition and procurement.</li></ul>",
      "updateDate": "2026-02-23",
      "versionCode": "id119s2988"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2988is.xml"
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
      "title": "VITAL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VITAL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans' Infrastructure and Transformation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to bolster upgrades and infrastructure for lasting development at the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:16Z"
    }
  ]
}
```
