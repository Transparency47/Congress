# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4429
- Title: Connected Vehicle Security Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4429
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-28T17:35:47Z
- Update date including text: 2026-05-28T17:35:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4429",
    "number": "4429",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Connected Vehicle Security Act of 2026",
    "type": "S",
    "updateDate": "2026-05-28T17:35:47Z",
    "updateDateIncludingText": "2026-05-28T17:35:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T17:01:00Z",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AR"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "MO"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "MO"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4429is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4429\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Moreno (for himself and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of connected vehicles and related software and hardware associated with foreign adversaries.\n#### 1. Short title\nThis Act may be cited as the Connected Vehicle Security Act of 2026 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe United States automotive industry is critical to the national economy, supporting millions of jobs, supply chains, and advanced manufacturing. The introduction of vehicles and components controlled by foreign adversaries threatens United States economic security, industrial competitiveness, and technological leadership.\n**(2)**\nThe People\u2019s Republic of China has rapidly expanded its automotive manufacturing capacity and is increasingly targeting export markets. Despite having the largest market in the world, the People's Republic of China exports nearly 8,000,000 vehicles annually, approximately twice the volume exported by any other country, demonstrating the scale at which vehicles and components controlled by a foreign adversary may enter global markets, including the United States.\n**(3)**\nConnected vehicles incorporate advanced information and communications technologies that collect, process, and transmit vast amounts of sensitive data, including geolocation, operational, and personal information, and are capable of being remotely accessed and controlled.\n**(4)**\nIn Executive Order 13873 ( 50 U.S.C. 1701 note; relating to securing the information and communications technology and services supply chain), the President declared a national emergency with respect to the threat posed by foreign adversaries creating and exploiting vulnerabilities in information and communications technology and services.\n**(5)**\nThe access, control, or influence of vehicle connectivity systems or automated driving systems by foreign adversaries creates substantial economic and national security risks to the United States, including risks of surveillance, espionage, cyber intrusion, and disruption of critical infrastructure. Such risks fall within the scope of the national emergency described in Executive Order 13873 and pose an unacceptable threat to the security and resilience of the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Automated driving system**\nThe term automated driving system means hardware and software that, collectively, are capable of performing the entire dynamic driving task for a connected vehicle on a sustained basis, regardless of whether it is limited to a specific operational design domain.\n**(2) Connected vehicle**\n**(A) In general**\nExcept as provided by subparagraph (B), the term connected vehicle means a vehicle driven or drawn by mechanical power and manufactured primarily for use on public streets, roads, and highways, that\u2014\n**(i)**\nintegrates onboard networked hardware with automotive software systems to communicate via dedicated short-range communication, cellular telecommunications connectivity, satellite communication, or other wireless spectrum connectivity with any other network or device; or\n**(ii)**\nis designed, manufactured, or originally equipped to communicate via such methods, regardless of whether such capability is enabled, disabled, or removed at the time of importation, manufacture, sale, resale, or introduction of the vehicle into interstate commerce in the United States.\n**(B) Exclusion**\nThe term connected vehicle does not include a vehicle operated only on a rail line.\n**(3) Connected vehicle hardware**\nThe term connected vehicle hardware means\u2014\n**(A)**\na vehicle connectivity system; and\n**(B)**\nvehicle connectivity system hardware.\n**(4) Country of origin**\nThe term country of origin , with respect to an item, means the country\u2014\n**(A)**\nin which the item is manufactured; or\n**(B)**\nthe government of which owns or controls, or has jurisdiction or direction over\u2014\n**(i)**\nthe entity manufacturing the item; or\n**(ii)**\nthe entity supplying the item.\n**(5) Covered country**\nThe term covered country means\u2014\n**(A)**\nthe Democratic People's Republic of North Korea;\n**(B)**\nthe People's Republic of China;\n**(C)**\nthe Russian Federation; and\n**(D)**\nthe Islamic Republic of Iran.\n**(6) Covered software**\nThe term covered software \u2014\n**(A)**\nmeans the software-based components installed in or on a connected vehicle, or designed to be installed in or on a connected vehicle, including application, middleware, and system software, executed by the primary processing unit or units of an item that directly enables the function of a vehicle connectivity system or automated driving system at the vehicle level; and\n**(B)**\nincludes any machine-learning model or other artificial intelligence component that directly enables decision-making or control of an automated driving system at the vehicle level.\n**(7) Electric vehicle**\nThe term electric vehicle has the meaning given that term in section 3 of the Electric and Hybrid Vehicle Research, Development, and Demonstration Act of 1976 ( 15 U.S.C. 2502 ).\n**(8) Importation**\nThe term importation has the meaning given the term import in section 1001 of the Controlled Substances Import and Export Act ( 21 U.S.C. 951 ).\n**(9) Resale**\n**(A) In general**\nThe term resale , with respect to an item, means the transfer of ownership of the item by an individual or entity that acquired the item for the purpose of transfer in the ordinary course of business, and not for the use of or consumption by the individual or entity.\n**(B) Exclusion**\nThe term resale does not include the transfer of a connected vehicle that was previously titled or registered to, and used by, a consumer or end-user or was acquired for bona fide use, lease, or operation by the individual or entity transferred the vehicle.\n**(10) Safety equipment**\nThe term safety equipment , with respect to a vehicle, means air bags, air bag inflators, and seatbelt systems.\n**(11) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Under Secretary of Commerce for Industry and Security.\n**(12) Transaction**\nThe term transaction \u2014\n**(A)**\nmeans any acquisition, importation, transfer, installation, dealing in, or use of any item subject to a prohibition under section 4(a), including ongoing activities, such as managed services, data transmission, software updates, repairs, or the platforming or data hosting of applications for consumer download; and\n**(B)**\nincludes\u2014\n**(i)**\nany other transaction, the structure of which is designed or intended to evade or circumvent this Act; and\n**(ii)**\na class of transactions.\n**(13) Vehicle connectivity system**\nThe term vehicle connectivity system means a vehicle connectivity system hardware or covered software item installed in or on a connected vehicle, or designed to be installed in or on a connected vehicle, that directly enables the function of transmission, receipt, conversion, or processing of radio frequency communications at a frequency over 450 megahertz.\n**(14) Vehicle connectivity system hardware**\nThe term vehicle connectivity system hardware \u2014\n**(A)**\nmeans software-enabled or programmable components that\u2014\n**(i)**\nare installed in or on a connected vehicle or designed to be installed in or on a connected vehicle;\n**(ii)**\nare directly connected to a vehicle connectivity system; and\n**(iii)**\ndirectly enable the function of a vehicle connectivity system or are part of an item that directly enables the function of a vehicle connectivity system; and\n**(B)**\nincludes\u2014\n**(i)**\nmicrocontrollers, microcomputers or modules, systems on a chip, networking or telematics units, cellular modem/modules, Wi-Fi microcontrollers or modules, Bluetooth microcontrollers or modules, satellite communication systems, other wireless communication microcontrollers or modules, external antennas, digital signal processors, and field-programmable gate arrays;\n**(ii)**\nelectronic systems integrated into a battery that directly enable or control the monitoring, management, security, or external communication of battery performance or operation, including any transmitter or interface component that performs such functions; and\n**(iii)**\nsafety equipment.\n#### 4. Prohibition on connected vehicles and other transactions that threaten economic or national security\n##### (a) Prohibitions\n**(1) Connected vehicles**\nOn and after January 1, 2027, the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of a connected vehicle is prohibited if\u2014\n**(A)**\nthe country of origin of the connected vehicle is a covered country or the connected vehicle is designed within a covered country, without regard to whether\u2014\n**(i)**\nat the time of importation, sale, resale, or introduction, the vehicle is equipped with any covered software or connected vehicle hardware subject to a prohibition under paragraph (2) or (3); or\n**(ii)**\nany such covered software or connected vehicle hardware\u2014\n**(I)**\nis removed from the vehicle before importation, sale, resale, or introduction; or\n**(II)**\nwill be installed after importation, sale, resale, or introduction; or\n**(B)**\nthe manufacturer of the connected vehicle is a joint venture, subsidiary, or other entity in which more than 15 percent of the equity interest, voting interest, board representation, or other indicia of control, whether directly or indirectly, is owned or controlled by an entity, or combination of entities, organized under the laws of, or with its principal place of business in, a covered country.\n**(2) Covered software**\nOn and after January 1, 2027, the integration of covered software into a connected vehicle that is imported, manufactured, sold, resold, or introduced into interstate commerce into the United States is prohibited if\u2014\n**(A)**\nthe country of origin of the covered software is a covered country; or\n**(B)**\nthe developer of the software\u2014\n**(i)**\nis organized under the laws of, or has its principal place of business in, a covered country; or\n**(ii)**\nis a joint venture, subsidiary, or other entity in which more than 25 percent of the equity interest, voting interest, board representation, or other indicia of control, whether directly or indirectly, is owned or controlled by an entity, or combination of entities, described in clause (i).\n**(3) Connected vehicle hardware**\n**(A) In general**\nOn and after January 1, 2030, the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of any connected vehicle hardware is prohibited if\u2014\n**(i)**\nthe country of origin of the hardware is a covered country; or\n**(ii)**\nthe manufacturer of the hardware\u2014\n**(I)**\nis organized under the laws of, or has its principal place of business in, a covered country; or\n**(II)**\nis a joint venture, subsidiary, or other entity in which more than 25 percent of the equity interest, voting interest, board representation, or other indicia of control, whether directly or indirectly, is owned or controlled by an entity, or combination of entities, described in subclause (I).\n**(B) Repair and warranty**\nThe prohibition under subparagraph (A) shall not apply to connected vehicle hardware that is imported, manufactured, sold, resold, or introduced into interstate commerce in the United States for the purpose of repair or under warranty for a connected vehicle with a model year before model year 2030.\n**(4) Additional items**\nSubject to an applicable ruling or advisory opinion issued under subsection (d), a prohibition under paragraph (1), (2), or (3) applies with respect to a connected vehicle, covered software, or connected vehicle hardware, as the case may be, that is renamed, rebranded, restructured, or altered to circumvent the prohibition.\n**(5) Exception**\nThe prohibitions under paragraphs (1), (2), and (3) shall not apply to the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of a connected vehicle, covered software, or connected vehicle hardware, as the case may be, for the sole purpose of testing and evaluation by an entity that\u2014\n**(A)**\nis organized under the laws of a State in the United States;\n**(B)**\ndoes not have its principal place of business in a covered country; and\n**(C)**\nis not 25 percent or more, whether directly or indirectly, owned or controlled by an entity, or combination of entities, organized under the laws of, or with its principal place of business in, a covered country.\n##### (b) Related transactions\n**(1) In general**\nThe Secretary shall prescribe regulations, pursuant to section 553 of title 5, United States Code, to prohibit any specific transaction relating to connected vehicles, including the importation, sale, distribution, integration, or use of a connected vehicle, covered software, connected vehicle hardware, or any other item subject to a prohibition under subsection (a), that the Secretary determines poses an undue or unacceptable threat to the economic or national security of the United States.\n**(2) Notice**\nIf the Secretary prohibits a transaction under paragraph (1), the Secretary shall deliver, by certified United States mail, to the parties to the transaction a notice of the prohibition that includes an identification, by name, of the specific item that the Secretary determines poses an undue or unacceptable threat to the economic or national security of the United States.\n##### (c) Authorizations\n**(1) Issuance**\n**(A) In general**\nThe Secretary, in consultation with the Secretary of Defense, the Secretary of Transportation, the Secretary of State, and the Secretary of Energy, may issue a general or specific authorization for the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of an item that would otherwise be subject to the prohibitions under subsection (a) if\u2014\n**(i)**\nthe Secretary determines, based on clear and convincing evidence and a written risk assessment, that the importation, manufacture, sale, resale, or introduction of the item does not pose, and is not reasonably likely to pose\u2014\n**(I)**\nan undue risk of data exfiltration from, or remote manipulation or operation of, a connected vehicle;\n**(II)**\na risk to critical infrastructure or the integrity of the industrial base of the United States; or\n**(III)**\nany other risk to the national security of the United States;\n**(ii)**\nnot less than 60 days before the authorization takes effect, the Secretary submits to Congress a detailed written notification, including the determination under clause (i) and underlying analysis, including the written risk assessment; and\n**(iii)**\nduring the 60-day period described in clause (ii), there is not enacted into law a joint resolution of disapproval with respect to the authorization of the item.\n**(B) Continued validity and modification and revocation of authorizations**\n**(i) Continued validity of existing authorizations**\nExcept as provided by clauses (ii) and (iii), any general or specific authorization issued under subparagraph (A) or subpart D of part 791 of title 15, Code of Federal Regulations, before January 1, 2030, shall remain in effect until January 1, 2032, unless modified, suspended or revoked under clause (ii).\n**(ii) Modification or revocation of general or specific authorizations**\nThe Secretary may, at any time, modify, suspend, or revoke a general or specific authorization described in clause (i) if the Secretary\u2014\n**(I)**\ndetermines that the authorization no longer satisfies the requirements of subparagraph (A)(i); and\n**(II)**\nprovides the public with an opportunity to comment before modifying, suspending, or revoking the authorization.\n**(2) Publication of list of authorized items**\n**(A) In general**\nThe Secretary shall publish, pursuant to section 553 of title 5, United States Code, and maintain a list of the items the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of which is authorized under paragraph (1). The initial such list shall be published not later than January 1, 2027.\n**(B) Inclusions**\n**(i) In general**\nTo the extent possible, the Secretary shall include, in the list required by subparagraph (A), the manufacturer and product name for each item on the list.\n**(ii) Other identifying characteristics**\nWhen it is not possible to include, in the list required by subparagraph (A), the manufacturer and product name for an item, the Secretary shall provide technical criteria sufficient to enable the automotive industry and importers to determine without undue difficulty whether the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of an item is authorized under paragraph (1). In carrying out this clause, the Secretary shall protect intellectual property to the extent practicable.\n**(iii) Risk assessment**\nTo the extent possible, the Secretary shall include, in the list required by subparagraph (A), a detailed explanation about why each item on the list does not pose an undue risk described in subparagraph (A) or (B) of paragraph (1).\n**(3) Requests for authorization**\nNot later than January 1, 2027, the Secretary shall establish a procedure pursuant to which an importer, manufacturer, supplier, or seller or reseller may seek the authorization under paragraph (1) of the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of an item described in subsection (a) that would otherwise be subject to the prohibitions under that subsection.\n##### (d) Rulings and advisory opinions\n**(1) In general**\nNot later than January 1, 2027, the Secretary shall establish a procedure pursuant to which an importer, manufacturer, or seller or reseller may seek a binding ruling or advisory opinion with respect to whether\u2014\n**(A)**\nthe importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of an item is or is not prohibited under this section; or\n**(B)**\na connected vehicle, covered software, or connected vehicle hardware has been renamed, rebranded, restructured, or altered to circumvent the prohibitions under subsection (a).\n**(2) Timing**\nThe Secretary shall issue a ruling or advisory opinion under paragraph (1) with respect to an item not later than 45 days after receiving an application supported by a reasonably clear description of the item.\n**(3) Publication**\n**(A) In general**\nThe Secretary shall\u2014\n**(i)**\npublish a list of the items for which the Secretary has issued rulings and advisory opinions under paragraph (1); and\n**(ii)**\nupdate that list not less frequently than annually.\n**(B) Prohibition on publication of identifying information**\nThe Secretary shall not publish the name of, or other information that might reasonably identify, the party that requested the ruling or advisory opinion.\n**(4) Continued validity of existing rulings and opinions**\nExcept as provided by paragraph (5), a ruling or advisory opinion issued under this subsection or subpart D of part 791 of title 15, Code of Federal Regulations, before January 1, 2027, shall remain in effect.\n**(5) Modification or revocation**\nThe Secretary may modify, suspend, or revoke any binding ruling or advisory opinion issued under paragraph (1) or subpart D of part 791 of title 15, Code of Federal Regulations, with respect to an item at any time if the Secretary determines that the circumstances that led to the ruling or opinion have changed.\n##### (e) Declaration of conformity\nThe Secretary shall establish a process under which a person that imports, manufactures, sells, resells, or introduces into interstate commerce in the United States a connected vehicle or connected vehicle hardware is required to submit a declaration, to be known as a declaration of conformity , to the Secretary before importing, manufacturing, selling, reselling, or introducing the vehicle or hardware that certifies that the vehicle or hardware is not subject to a prohibition under subsection (a).\n##### (f) Civil penalties\n**(1) In general**\nThe Secretary shall assess a civil penalty for each transaction that is a violation of a prohibition under subsection (a) in an amount that is not less than the greater of\u2014\n**(A)**\n$1,500,000; or\n**(B)**\nfive times the value of the transaction.\n**(2) Continuing violations**\nIn the case of a violation that occurs on more than one day, each day on which the violation continues shall be treated as a separate violation.\n##### (g) Classified information\nThe Secretary may rely on classified information in carrying out this section, which may be submitted to a reviewing court ex parte and in camera.\n##### (h) Petitions for review\nThe filing in a court of a petition for review shall not stay the effectiveness of any action under this section unless ordered by the court.\n#### 5. Use of existing advisory bodies; interagency coordination\n##### (a) Use of existing advisory bodies\n**(1) In general**\nIn carrying out this Act, the Secretary may consult, as appropriate, with existing advisory committees of the Department of Transportation and other relevant Federal agencies, including the Advisory Committee on Automation in Transportation, on matters relating to connected vehicles and associated national security risks.\n**(2) Scope of consultation**\nConsultation under paragraph (1) may include consideration of\u2014\n**(A)**\nrisks relating to data security, cybersecurity, and supply chain integrity associated with connected vehicles;\n**(B)**\nthe effectiveness of authorities and regulations issued under this Act;\n**(C)**\nemerging technologies and threat vectors relevant to connected vehicle ecosystems; and\n**(D)**\nrecommendations made to the Secretary with respect to regulatory, enforcement, and policy measures to mitigate risks described in subparagraph (A).\n##### (b) Interagency coordination\nIn carrying out this Act, the Secretary may consult and coordinate, as appropriate, with the Federal Communications Commission and other relevant Federal agencies to ensure alignment with respect to the scope, timeline, and implementation of any prohibitions or restrictions issued under this Act, including to avoid duplicative, inconsistent, or conflicting regulatory requirements.\n#### 6. Reports\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary shall submit to Congress a report\u2014\n**(1)**\ndescribing activities carried out to enforce the prohibitions under section 4, including enforcement actions taken and resources utilized;\n**(2)**\nproviding a detailed accounting of items covered by such prohibitions during the 1-year period preceding submission of the report;\n**(3)**\nexplaining any exclusions, exemptions, or determinations made by the Secretary, including the rationale and criteria applied;\n**(4)**\nassessing the effectiveness of such prohibitions in decreasing the threats to the economic and national security of the United States posed by connected vehicles;\n**(5)**\nincluding metrics on enforcement, compliance rates, violations identified, penalties assessed, and any identified gaps or challenges; and\n**(6)**\nmaking recommendations with respect to further decreasing such threats.\n#### 7. Severability; regulatory continuity\n##### (a) Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act, and the application of the remaining provisions to any person or circumstance, shall not be affected.\n##### (b) Restoration of prior regulations\nIf a court of competent jurisdiction enters a final judgment holding invalid or unenforceable a provision of this Act and supersedes regulations prescribed to carry out section 4, the Secretary may, notwithstanding any other provision of this Act, reissue or reinstate, in whole or in part, any similar regulations that were in effect on the day before the date of the enactment of this Act.\n#### 8. Interaction with regulations\n##### (a) Rule of construction\nNothing in this Act shall be construed to prohibit, limit, or otherwise affect the authority of the Secretary of Commerce to implement or administer subpart D of part 791 of title 15, Code of Federal Regulations, as added by the final rule of the Bureau of Industry and Security entitled Securing the Information and Communications Technology and Services Supply Chain: Connected Vehicles (90 Fed. Reg. 5360).\n##### (b) Delayed implementation for software and hardware not covered by regulations\nIn the case of covered software and connected vehicle hardware that is subject to a prohibition under paragraph (2) or (3) of section 4(a) and is not subject to subpart D of part 791 of title 15, Code of Federal Regulations, as in effect on the day before the date of the enactment of this Act, the Secretary shall implement the prohibition under section 4(a) after January 1, 2030, and before January 1, 2032.\n##### (c) Treatment of prior exclusions\n**(1) In general**\nSubject to paragraph (2), any exclusion or exception to a prohibition under subpart D of part 791 of title 15, Code of Federal Regulations, as in effect on the day before the date of the enactment of this Act, shall remain valid and shall apply to the prohibitions under section 4(a).\n**(2) Rulemaking**\nBeginning January 1, 2030, the Secretary shall conduct a rulemaking, pursuant to section 553 of title 5, United States Code, to determine whether exclusions or exceptions described in paragraph (1) should be continued, modified, or terminated for the purposes of this Act.",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-05-11",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, and Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8730",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Connected Vehicle Security Act of 2026",
      "type": "HR"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-05-19T16:14:52Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4429is.xml"
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
      "title": "Connected Vehicle Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Connected Vehicle Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the importation, manufacture, sale, resale, or introduction into interstate commerce in the United States of connected vehicles and related software and hardware associated with foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:29Z"
    }
  ]
}
```
